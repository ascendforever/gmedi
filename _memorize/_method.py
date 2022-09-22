from __future__ import annotations

__all__ = [
    'MemorizedMethod',
    'memorize_method',
    'MemorizedMethodFirst',
    'memorize_method_first',
]

from gmedi.__common import *
from gmedi.__static import *

class MemorizedMethodBase(t.Generic[T], metaclass=abc.ABCMeta):
    __slots__ = ('func', '_bound_method_type', '__weakref__')
    __match_args__ = ('func', '_bound_method_type')
    def __init_subclass__(cls, **kwargs) -> None:
        # noinspection PyUnresolvedReferences
        if not hasattr(cls, 'apply') or not isinstance(cls.apply, abcs.Callable):
            raise TypeError("Subclasses must have a method called `apply`")
    @classmethod
    @t.final
    def with_proper_repr(cls:MemorizedMethodBase[T], func:abcs.Callable[..., T]) -> MemorizedMethodBase[T]:
        """Creates memorized method, calls `cls.enable_proper_repr`, and returns memorized method"""
        # noinspection PyUnresolvedReferences
        self:MemorizedMethodBase[T] = cls.apply(func)
        self.enable_proper_repr()
        return self
    @abc.abstractmethod
    def __repr__(self) -> str: ...
    @classmethod
    @abc.abstractmethod
    def supports(cls, clsm, /) -> bool: ...
    @classmethod
    def supporting(cls, clsm:T, /) -> T:
        """Decorator to check whether a class is supported"""
        if not cls.supports(clsm):
            raise TypeError(f"Class does not support {cls.__name__}")
        return clsm
    # noinspection PyMethodParameters
    @abc.abstractmethod
    def force(self_mm:MemorizedMethodBase[T], self, /, *args, **kwargs) -> T: ...
    # noinspection PyMethodParameters
    @abc.abstractmethod
    def __call__(self_mm:MemorizedMethodBase[T], self, /, *args, **kwargs) -> T: ...
    # @abc.abstractmethod
    # def __get__(self:MemorizedMethodBase[T], instance, owner): ...
    @t.final
    def __get__(self:MemorizedMethodBase[T], instance, owner) -> _MMBoundMethod[T] | MemorizedMethodBase[T]:
        if instance is None:
            return self
        if self._bound_method_type is None:
            return _MMBoundMethod(self, instance)
        return self._bound_method_type(self, instance)
    @t.final
    def enable_proper_repr(self:MemorizedMethodBase[T], /) -> None:
        """
        This method should be used when a proper repr for bound methods is desired, otherwise it will just waste processing power
        If not called yet, creates a subclass of `_MMBoundMethod` which has `__call__` masked as the source memorized method (using `functools.update_wrapper`)
        This subclass will be used when `__get__` is called so that the bound method's `__call__` has a signature and docstring that makes perfect sense
        If already called, does nothing
        """
        if self._bound_method_type is None:
            def exec_body(ns:dict[str,t.Any]) -> None:
                ns['__call__'] = functools.wraps(self.func)(_MMBoundMethod.__call__)
            # noinspection PyAttributeOutsideInit
            self._bound_method_type = types.new_class('__bound_memorized_method_wrapper_UNIQUE', bases=(_MMBoundMethod,), kwds={}, exec_body=exec_body)

class _MemorizedMethodNT(t.NamedTuple):
    arg_hash:int
    result:t.Any
    bound_inst_weakrefs:weakref.WeakSet

class MemorizedMethod(t.Generic[T], MemorizedMethodBase[T]):
    """Memorize a single result for a method, for each instantiation
    If one instance has the same hash as another, it make use the other's cached result
    Class must be hashable and weak-reference-able
    Use classmethod `apply` for easy creation when decorating, do not instantiate normally
    [Created 6/26/21]"""
    __slots__ = ('include_self_for_hashing','weakref_results','cache','excluded_kwargs','pref')
    __match_args__ = MemorizedMethodBase.__match_args__ + __slots__
    def __init__(self:MemorizedMethod[T], *, func:abcs.Callable[..., T], excluded_kwargs:t.Optional[tuple[str, ...]]=None, include_self_for_hashing:bool=True, weakref_results:bool=False, auto_clean:bool=True):
        self.func:t.Final[abcs.Callable[..., T]] = func
        self.include_self_for_hashing:t.Final[bool] = include_self_for_hashing
        self.weakref_results:t.Final[bool] = weakref_results
        self.cache:t.Final[dict[int,_MemorizedMethodNT]] = {}
        self.excluded_kwargs:t.Final[t.Optional[tuple[str, ...]]] =excluded_kwargs
        self.pref:t.Final[abcs.Callable[[dict[str,t.Any]], None]] = (
            (self.__pref_clean_only if excluded_kwargs is None else self.__pref_both)
            if auto_clean else
            (self.__pref_neither    if excluded_kwargs is None else self.__pref_exclude_only)
        )
        self._bound_method_type:t.Optional[t.Type[_MMBoundMethod]] = None
    @classmethod
    def supports(cls, clsm, /) -> bool:
        """Check if a class supports method memorization
        Checks whether the class is vhashable and weak-reference-able"""
        return isinstance(clsm, VHashable) and hasattr(clsm, '__weakref__')
    def __repr__(self:MemorizedMethod[T], /) -> str:
        return f"{self.__class__.__name__}(func={self.func!r}, excluded_kwargs={self.excluded_kwargs=!r}, " \
               f"include_self_for_hashing={self.include_self_for_hashing=!r}, weakref_results={self.weakref_results=!r}, auto_clean={self.auto_cleaning})"
    @property
    def auto_cleaning(self, /) -> bool:
        return self.pref is self.__pref_both or self.pref is self.__pref_clean_only
    def user_creation_repr(self:MemorizedMethod[T], /) -> str:
        """Repr corresponding to instantiation using MemorizedMethod.apply (convenience creation method)"""
        return f"{self.__class__.__name__}.{self.__class__.apply.__name__}({self.func!r}, {', '.join(map(repr, self.excluded_kwargs))}, " \
               f"include_self_for_hashing={self.include_self_for_hashing!r}, weakref_results={self.weakref_results!r}, auto_clean={self.auto_cleaning}"
    try:
        _msc = MatchingSignatureChecker()
    except NameError as e:
        if platform.system()=='Windows':
            raise e
        # noinspection PyProtectedMember
        from gll.__static.__static1.__static2.__static3.__static4._matching_sig import MatchingSignatureChecker
        _msc = MatchingSignatureChecker()
    with _msc:
        @_msc
        def __pref_both(self:MemorizedMethod[T], /, kwargs:dict[str,t.Any]) -> None:
            self.clean_cache()
            for p in self.excluded_kwargs:
                kwargs.pop(p, None)
        @_msc
        def __pref_clean_only(self:MemorizedMethod[T], /, kwargs:dict[str,t.Any]) -> None: # noqa unused local
            self.clean_cache()
        @_msc
        def __pref_exclude_only(self:MemorizedMethod[T], /, kwargs:dict[str,t.Any]) -> None:
            for p in self.excluded_kwargs:
                kwargs.pop(p, None)
        @_msc
        def __pref_neither(self:MemorizedMethod[T], /, kwargs:dict[str,t.Any]) -> None:
            pass
    del _msc
    def __len__(self:MemorizedMethod[T], /) -> int:
        return len(self.cache)
    def _intro(self:MemorizedMethod[T], inst:VHashable, /, args:tuple, kwargs:dict[str,t.Any]) -> tuple[int,_MemorizedMethodNT,int]:
        self.pref(kwargs)
        original_self_hash:t.Final[int] = vhash(inst)
        data:_MemorizedMethodNT = self.cache.get(original_self_hash, None)
        arg_hash = hash((original_self_hash, args, *kwargs.values())) if self.include_self_for_hashing else \
                   hash((                    args, *kwargs.values()))
        return original_self_hash, data, arg_hash
    # noinspection PyMethodParameters
    def force(self_mm:MemorizedMethod[T], self:VHashable, /, *args, **kwargs) -> T:
        """Force calculate, even if cached result is obtainable"""
        original_self_hash, data, arg_hash = self_mm._intro(self, args=args, kwargs=kwargs) # type: int, _MemorizedMethodNT, int
        result = self_mm.func(self, *args, **kwargs)
        ws = weakref.WeakSet([self])
        if data is not None:
            ws.update(data.bound_inst_weakrefs)
        self_mm.cache[original_self_hash] = _MemorizedMethodNT(
            arg_hash,
            (weakref.ref(result) if self_mm.weakref_results else result),
            ws
        )
        return result
    # noinspection PyMethodParameters
    def __call__(self_mm:MemorizedMethod[T], self:VHashable, /, *args, **kwargs) -> T:
        original_self_hash, data, arg_hash = self_mm._intro(self, args=args, kwargs=kwargs) # type: int, _MemorizedMethodNT, int
        if (data is None) or (data.arg_hash != arg_hash) or (self_mm.weakref_results and data.result() is None):
            result = self_mm.func(self, *args, **kwargs)
            # we need to recalc hash of self_mm because the method may change the hash! # uh no i dont tihnk so anymore
            self_mm.cache[original_self_hash] = _MemorizedMethodNT(
                arg_hash,
                (weakref.ref(result) if self_mm.weakref_results else result),
                weakref.WeakSet([self])
            )
            return result
        data.bound_inst_weakrefs.add(self)
        if self_mm.weakref_results:
            return data.result()
        return data.result
    def clean_cache(self:MemorizedMethod[T], /) -> int:
        """Remove entries in cache that are not bound to instances
        Returns the number of deleted cache entries"""
        cache = self.cache # remove unnecessary __getattr__s
        to_del = array.array('q', (hsh for hsh,nt in cache.items() if len(nt.bound_inst_weakrefs)==0))
        for k in to_del:
            del cache[k]
        return len(to_del)
    def clear_cache(self:MemorizedMethod[T], /) -> int:
        """Returns the number of deleted cache entries"""
        cache = self.cache # remove unnecessary __getattr__s
        res:int = len(cache)
        cache.clear()
        return res
    # @classmethod
    # def _make(cls:t.Type[MemorizedMethod[T]], /, func:t.Optional[abcs.Callable], *, excluded_kwargs:tuple[str], include_self_for_hashing:bool, weakref_results:bool, auto_clean:bool) -> t.Union[MemorizedMethod[T] , functools.partial[abcs.Callable]]:
    #     if isinstance(func, str):
    #         excluded_kwargs = (func, *excluded_kwargs)
    #         func = None
    #     elif excluded_kwargs is not None and len(excluded_kwargs)==0:
    #         excluded_kwargs = None
    #     if func is None:
    #         return functools.partial(cls._make, excluded_kwargs=excluded_kwargs, include_self_for_hashing=include_self_for_hashing, weakref_results=weakref_results, auto_clean=auto_clean)
    #     self = super().__new__(cls)
    #     cls.__init__(self, func=func, excluded_kwargs=excluded_kwargs, include_self_for_hashing=include_self_for_hashing, weakref_results=weakref_results, auto_clean=auto_clean)
    #     return self
    # @t.overload
    # def __new__(cls:t.Type[MemorizedMethod[T]], func:abcs.Callable[..., weakref.ReferenceType] , /, *excluded_kwargs:str, include_self_for_hashing:bool=True, weakref_results:t.Literal[True]=True, auto_clean:bool=True) -> MemorizedMethod[T]:
    #     ...
    # @t.overload
    # def __new__(cls:t.Type[MemorizedMethod[T]], func:abcs.Callable , /, *excluded_kwargs:str, include_self_for_hashing:bool=True, weakref_results:bool=False, auto_clean:bool=True) -> MemorizedMethod[T]:
    #     ...
    # @t.overload
    # def __new__(cls:t.Type[MemorizedMethod[T]], func:t.Type[None]=None, /, *excluded_kwargs:str, include_self_for_hashing:bool=True, weakref_results:bool=False, auto_clean:bool=True) -> abcs.Callable[[abcs.Callable], MemorizedMethod[T]]:
    #     ...
    # def __new__(cls:t.Type[MemorizedMethod[T]], func:t.Optional[abcs.Callable]=None, /, *excluded_kwargs:str, include_self_for_hashing:bool=True, weakref_results:bool=False, auto_clean:bool=True) -> t.Union[MemorizedMethod[T] , functools.partial[abcs.Callable]]:
    #     """Lenient creation function; Ideal for when using @ decoration"""
    #     return cls._make(func=func, excluded_kwargs=excluded_kwargs, include_self_for_hashing=include_self_for_hashing, weakref_results=weakref_results, auto_clean=auto_clean)
    @classmethod
    def _make(cls:t.Type[MemorizedMethod[T]], /, func:None|abcs.Callable, *, excluded_kwargs:tuple[str,...], include_self_for_hashing:bool, weakref_results:bool, auto_clean:bool) -> MemorizedMethod[T] | functools.partial[abcs.Callable]:
        if isinstance(func, str):
            excluded_kwargs = (func, *excluded_kwargs)
            func = None
        elif excluded_kwargs is not None and len(excluded_kwargs)==0:
            excluded_kwargs = None
        if func is None:
            return functools.partial(cls._make, excluded_kwargs=excluded_kwargs, include_self_for_hashing=include_self_for_hashing, weakref_results=weakref_results, auto_clean=auto_clean)
        return cls(func=func, excluded_kwargs=excluded_kwargs, include_self_for_hashing=include_self_for_hashing, weakref_results=weakref_results, auto_clean=auto_clean)
    @classmethod
    @t.overload
    def apply(cls:t.Type[MemorizedMethod[T]], func:abcs.Callable[..., weakref.ReferenceType] , /, *excluded_kwargs:str, include_self_for_hashing:bool=True, weakref_results:t.Literal[True]=True, auto_clean:bool=True) -> MemorizedMethod[T]:
        ...
    @classmethod
    @t.overload
    def apply(cls:t.Type[MemorizedMethod[T]], func:abcs.Callable , /, *excluded_kwargs:str, include_self_for_hashing:bool=True, weakref_results:bool=False, auto_clean:bool=True) -> MemorizedMethod[T]:
        ...
    @classmethod
    @t.overload
    def apply(cls:t.Type[MemorizedMethod[T]], func:t.Type[None]=None, /, *excluded_kwargs:str, include_self_for_hashing:bool=True, weakref_results:bool=False, auto_clean:bool=True) -> abcs.Callable[[abcs.Callable], MemorizedMethod[T]]:
        ...
    @classmethod
    def apply(cls:t.Type[MemorizedMethod[T]], func:t.Optional[abcs.Callable]=None, /, *excluded_kwargs:str, include_self_for_hashing:bool=True, weakref_results:bool=False, auto_clean:bool=True) -> MemorizedMethod[T] | functools.partial[abcs.Callable]:
        """Lenient creation function; Ideal for when using @ decoration"""
        return cls._make(func=func, excluded_kwargs=excluded_kwargs, include_self_for_hashing=include_self_for_hashing, weakref_results=weakref_results, auto_clean=auto_clean)

memorize_method = MemorizedMethod.apply

class _MMBoundMethod(t.Generic[T], abcs.Callable[..., T]):
    __slots__ = __match_args__ = ('mm','owner')
    def __init__(self, /, mm:MemorizedMethodBase[T], owner:object):
        self.mm:t.Final[MemorizedMethodBase[T]] = mm
        self.owner:t.Final[object] = owner
    def __repr__(self, /) -> str:
        return f"<bound memorized method {self.mm.func.__qualname__} of {self.owner!r}>"
    def __call__(self, /, *args, **kwargs) -> T:
        return self.mm.__class__.__call__(self.mm, self.owner, *args, **kwargs)


class MemorizedMethodFirst(t.Generic[T], MemorizedMethodBase[T]):
    """Memorize a single result for a method, for each instantiation
    Prefer this over MemorizedMethod if possible, as it has less overhead in memory and speed
    Once calculated, will not be recalculated!
    Different instances do not share results
    Use classmethod `apply` for easy creation when decorating, do not instantiate normally
    [Created 11/4/21]"""
    __slots__ = ('name','saved')
    __match_args__ = MemorizedMethodBase.__match_args__ + __slots__
    def __init__(self:MemorizedMethodFirst[T], func:abcs.Callable[..., T], cached_result_name:str):
        self.func:t.Final[abcs.Callable[..., T]] = func
        self.name:t.Final[str] = cached_result_name
        self._bound_method_type:t.Optional[t.Type[_MMBoundMethod]] = None
    @classmethod
    def supports(cls, clsm, cached_result_name:str) -> bool:
        if hasattr(clsm, '__slots__'):
            return f'_cached_{cached_result_name}' in cls.__slots__
        return True
    @classmethod
    def supporting(cls, cached_result_name:str, /) -> T:
        """Decorator to check whether a class is supported"""
        def deco(clsm):
            if not cls.supports(clsm, cached_result_name):
                raise TypeError(f"Class does not support {cls.__name__}")
            return clsm
        return deco
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.func!r})"
    # noinspection PyMethodParameters
    def __call__(self_mm:MemorizedMethodFirst[T], self, /, *args, **kwargs) -> T:
        name = self_mm.name
        __sentinel = sentinel
        res = getattr(self, name, __sentinel)
        if res is __sentinel:
            # noinspection PyUnboundLocalVariable
            res = self_mm.func(self, *args, **kwargs)
            setattr(self, name, res)
        return res
    # noinspection PyMethodParameters
    def force(self_mm:MemorizedMethodFirst[T], self, /, *args, **kwargs) -> T:
        res = self_mm.func(self, *args, **kwargs)
        setattr(self, self_mm.name, res)
        return res
    @classmethod
    def _make(cls:t.Type[MemorizedMethodFirst[T]], /, func:t.Optional[abcs.Callable[...,T]], *, cached_result_name:t.Optional[str]) -> \
            MemorizedMethodFirst[T] | functools.partial[abcs.Callable[ [None|abcs.Callable[...,T]], MemorizedMethodFirst[T] ]]:
        if isinstance(func, str):
            cached_result_name = func
            func = None
        elif not cached_result_name:
            cached_result_name = f'_{func.__name__}'
        if func is None:
            return functools.partial(cls._make, cached_result_name=cached_result_name)
        return cls(func, cached_result_name=cached_result_name)
    @classmethod
    @t.overload
    def apply(cls:t.Type[MemorizedMethodFirst[T]], func:abcs.Callable[..., T], /, cached_result_name:t.Optional[str]=None) -> MemorizedMethodFirst[T]:
        ...
    @classmethod
    @t.overload
    def apply(cls:t.Type[MemorizedMethodFirst[T]], func:t.Type[None], /, cached_result_name:t.Optional[str]=None) -> abcs.Callable[[abcs.Callable[..., T]], MemorizedMethodFirst[T]]:
        ...
    @classmethod
    def apply(cls:t.Type[MemorizedMethodFirst[T]], func:abcs.Callable[..., T], /, cached_result_name:t.Optional[str]=None):
        return cls._make(func, cached_result_name=cached_result_name)

memorize_method_first = MemorizedMethodFirst.apply










# class _AsyncMemorizedMethod(t.Generic[T], _MemorizedMethod): # i dont like this because its rewritten code; if i need it, which i doubt, then ill implement, for now it need not exist
#     async def __call__(self:_AsyncMemorizedMethod, inst:abcs.Hashable, /, *args, **kwargs) -> T:
#         self.clean_cache()
#         if self.excluded_kwargs is not None:
#             for p in self.excluded_kwargs:
#                 kwargs.pop(p, None)
#         original_self_hash:t.Final[int] = hash(inst)
#         data:_MemorizedMethodNT = self.cache.get(original_self_hash, None)
#         arg_hash = hash((inst, args, *kwargs.values())) if self.include_self_for_hashing else \
#                    hash((      args, *kwargs.values()))
#         if data is None or data.arg_hash!=arg_hash or (data.result() is None if self.use_weakref_for_results else False):
#             result = await self.func(inst, *args, **kwargs)
#             # we need to recalc hash of self because the method may change the hash! # uh no i dont tihnk so anymore
#             self.cache[original_self_hash] = _MemorizedMethodNT( arg_hash , (weakref.ref(result) if self.use_weakref_for_results else result), {weakref.ref(inst),} )
#             return result
#         self.cache[original_self_hash].bound_inst_weakrefs.add(weakref.ref(inst))
#         ret = self.cache[original_self_hash].result
#         if self.use_weakref_for_results:
#             ret = ret()
#         return ret
# def __async_mm_helper(func:abcs.Callable=None, *, excluded:t.Optional[tuple[str, ...]]=None, include_self:bool=True, use_weakref:bool=False):
#     if isinstance(func, str):
#         excluded = (func, *excluded)
#         func = None
#     elif excluded is not None and len(excluded)==0:
#         excluded = None
#     if func is None:
#         return functools.partial(__mm_helper, excluded=excluded, include_self=include_self, use_weakref=use_weakref)
#     return _AsyncMemorizedMethod(func=func, excluded_kwargs=excluded, include_self_for_hashing=include_self, use_weakref_for_results=use_weakref)
# def async_memorized_method(func:abcs.Callable=None, /, *excluded:str, include_self:bool=True, use_weakref:bool=False):
#     """Memorize a single call to a method; Separate caches for separate instances
#     `excluded` are the excluded keyword arguments
#     [Created 6/26/21]"""
#     return __async_mm_helper(func, excluded=excluded, include_self=include_self, use_weakref=use_weakref)










# def instance_memorized(func:abcs.Callable=None, /, *excluded:str, include_self:bool=True, use_weakref:bool=False):
#     """Memorize a single call to a method; Separate caches for separate instances
#     `excluded` are the excluded keyword arguments
#     [Created 6/7/21]"""
#     if isinstance(func, str):
#         excluded = (func, *excluded)
#         func = None
#     elif len(excluded)==0:
#         excluded = None
#     excluded:t.Optional[tuple[str,...]]
#     cache:dict[int,_MemorizedMethodNT] = {}
#     # noinspection PyShadowingNames
#     def deco(func:abcs.Callable, /):
#         @functools.wraps(func)
#         def wrapper(self, /, *args, **kwargs):
#             nonlocal cache
#             wrapper.clean_cache()
#             if excluded is not None:
#                 for p in excluded:
#                     kwargs.pop(p, None)
#             original_self_hash:t.Final[int] = hash(self)
#             data = cache.get(original_self_hash, None)
#             arg_hash = hash((self, args, kwargs.values())) if include_self else \
#                        hash((      args, kwargs.values()))
#             if data is None or data.hash!=arg_hash or (data.result() is None if use_weakref else False):
#                 result = func(self, *args, **kwargs)
#                 # we need to recalc hash of self because the method may change the hash! # uh no i dont tihnk so anymore
#                 cache[original_self_hash] = _MemorizedMethodNT( arg_hash , (weakref.ref(result) if use_weakref else result), weakref.ref(self) )
#                 return result
#             ret = cache[original_self_hash].result
#             if use_weakref:
#                 ret = ret()
#             return ret
#         def __f():
#             for k,v in [(k,v) for k,v in cache.items() if v.inst_weakref() is not None]:
#                 del cache[k]
#         wrapper.clean_cache = __f
#         return wrapper
#     return deco if func is None else deco(func)
