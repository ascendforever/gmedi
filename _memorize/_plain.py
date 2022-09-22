
__all__ = [
    'memorized',
]

from gmedi.__common import *
from gmedi.__static import *

def memorized(func:None|abcs.Callable=None, /, *excluded:str|int, weakref_results:bool=False):
    """Memorize the most recent call to a function
    Recalculates when argument hashes are not the same as the saved
    `excluded` are the excluded keyword arguments, or positional argument indexes
    [Created 6/7/21]"""
    do_excluded_args:bool = False
    do_excluded_kwargs:bool = False
    if not isinstance(func, abcs.Callable) or len(excluded)!=0:
        # noinspection PyPep8Naming
        T_func = type(func)
        if T_func is str or T_func is int:
            excluded = (func,*excluded)
            func = None
        del T_func
        excluded_args:t.Optional[frozenset[int]] = frozenset([obj for obj in excluded if isinstance(obj,int)])
        if len(excluded_args)==0:
            del excluded_args
        else:
            do_excluded_args = True
        excluded_kwargs:t.Optional[list[str]] = [obj for obj in excluded if isinstance(obj,str)]
        if len(excluded_kwargs)==0:
            del excluded_kwargs
        else:
            do_excluded_kwargs = True
    del excluded
    saved_hash:int = ...
    saved:t.Any = None
    def deco(func:abcs.Callable, /): # noqa shadowing
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal saved_hash,saved
            if do_excluded_kwargs:
                __popper = kwargs.pop
                for p in excluded_kwargs:
                    __popper(p, None)
                del __popper
            if do_excluded_args:
                arg_hash:int = hash((tuple(arg for i,arg in enumerate(args) if i not in excluded_args), kwargs.values()))
            else:
                arg_hash:int = hash((args, kwargs.values()))
            # from timeit import timeit
            # print(timeit('x is y', setup='x=1;y=1'))
            # print(timeit('x==y',   setup='x=1;y=1'))
            # Conclusion? USE `is` when comparing integers
            if arg_hash is saved_hash or (weakref_results and saved() is None):
                saved_hash = arg_hash
                result = func(*args, **kwargs)
                saved = weakref.ref(result) if weakref_results else result
                return result
            return saved() if weakref_results else saved
        return wrapper
    return deco if func is None else deco(func)
