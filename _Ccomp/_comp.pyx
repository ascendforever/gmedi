
__all__ = [
    'bz2_decompress_conditional',
    'bz2_compress_conditional',
    'bz2_decompress_conditional_split',
    'bz2_compress_conditional_split',
    'lzma_decompress_conditional',
    'lzma_compress_conditional',
    'lzma_decompress_conditional_split',
    'lzma_compress_conditional_split',
    'gzip_decompress_conditional',
    'gzip_compress_conditional',
    'gzip_decompress_conditional_split',
    'gzip_compress_conditional_split',
    'CompressedString',
]

from gmedi.__common import *
from gmedi.__static import *

from glite.__cimports cimport *

cdef inline object _c_compress(object method, object b, bytes precompressed=None, float min_savings=0.10):
    precompressed = method(b) if precompressed is None else precompressed
    if len(precompressed)*(1+min_savings) > len(b):
        return b'\x00'+b
    return b'\x01' + precompressed
cdef inline object _c_decompress(object method, object b):
    b = memoryview(b) if isinstance(b, bytes) else b
    if b[0]==0x0:
        return b[1:]
    return method(bytes(b[1:]))
cdef inline bytes _c_decompress_split(object method, const bint decompress, object b):
    b = b if isinstance(b, bytes) else b.tobytes()
    if decompress:
        return method(b)
    return b
cdef inline tuple _c_compress_split(object method, object b, bytes precompressed=None, float min_savings=0.10):
    precompressed = method(b) if precompressed is None else precompressed
    if len(precompressed)*(1+min_savings) > len(b):
        return False, b
    return True, precompressed

cpdef object bz2_decompress_conditional(object b):                                                       return _c_decompress(      bz2.decompress, b)
cpdef object bz2_compress_conditional(object b, bytes precompressed=None, float min_savings=0.10):       return _c_compress(        bz2.decompress, b, precompressed=precompressed, min_savings=min_savings)
cpdef object bz2_decompress_conditional_split(const bint decompress, object b):                          return _c_decompress_split(bz2.decompress, decompress, b)
cpdef  tuple bz2_compress_conditional_split(object b, bytes precompressed=None, float min_savings=0.10): return _c_compress_split(  bz2.compress, b, precompressed=precompressed, min_savings=min_savings)

cpdef object lzma_decompress_conditional(object b):                                                       return _c_decompress(      lzma.decompress, b)
cpdef object lzma_compress_conditional(object b, bytes precompressed=None, float min_savings=0.10):       return _c_compress(        lzma.decompress, b, precompressed=precompressed, min_savings=min_savings)
cpdef object lzma_decompress_conditional_split(const bint decompress, object b):                          return _c_decompress_split(lzma.decompress, decompress, b)
cpdef  tuple lzma_compress_conditional_split(object b, bytes precompressed=None, float min_savings=0.10): return _c_compress_split(  lzma.compress, b, precompressed=precompressed, min_savings=min_savings)

cpdef object gzip_decompress_conditional(object b):                                                       return _c_decompress(      gzip.decompress, b)
cpdef object gzip_compress_conditional(object b, bytes precompressed=None, float min_savings=0.10):       return _c_compress(        gzip.decompress, b, precompressed=precompressed, min_savings=min_savings)
cpdef object gzip_decompress_conditional_split(const bint decompress, object b):                          return _c_decompress_split(gzip.decompress, decompress, b)
cpdef  tuple gzip_compress_conditional_split(object b, bytes precompressed=None, float min_savings=0.10): return _c_compress_split(  gzip.compress, b, precompressed=precompressed, min_savings=min_savings)




cdef class CompressedString:
    @classmethod
    def supports_lib(cls, object lib) -> bint:
        if lib is gzip or lib is lzma or lib is bz2: return True
        if not hasattr(lib, 'compress'): return False
        if not hasattr(lib, 'decompress'): return False
        cdef object compress = lib.compress
        cdef object decompress = lib.decompress
        if not inspect.isroutine(compress): return False
        if not inspect.isroutine(decompress): return False
        cdef object sig, annotation, curr
        cdef list params
        for f in [compress, decompress]:
            sig = inspect.signature(compress)
            annotation = sig.return_annotation
            if annotation!=inspect.Parameter.empty and annotation!=bytes: return False
            params = list(sig.parameters.values())
            if len(params)!=2:
                return False
            curr = params[0]
            annotation = curr._annotation
            if curr._name!='data': return False
            if annotation!=inspect.Parameter.empty and annotation!=bytes: return False
            curr = params[1]
            annotation = curr._annotation
            if curr._name!='compresslevel': return False
            if annotation!=inspect.Parameter.empty and annotation!=int: return False
            sig = inspect.signature(decompress)
            annotation = sig.return_annotation
            if annotation!=inspect.Parameter.empty and annotation!=bytes: return False

        cdef str name
        for name in dir(lib):
            if re.fullmatch(r"[a-zA-Z_]*Compressor", name):
                setattr(lib, '_CompressorAlias_for_gllCompressedString', getattr(lib, name))
                break
        else: return False
        cdef object Compressor = lib._CompressorAlias_for_gllCompressedString
        # for name in dir(lib):
        #     if re.fullmatch(r"\w+Decompressor", name):
        #         break
        # else: return False
        # cdef object Decompressor = getattr(lib, name)
        if not inspect.isclass(Compressor): return False
        # if not inspect.isclass(Decompressor): return False
        if not hasattr(Compressor, 'compress'): return False
        if not hasattr(Compressor, 'flush'): return False
        # if not hasattr(Decompressor, 'decompress'): return False

        sig = inspect.signature(Compressor.compress)
        annotation = sig.return_annotation
        if annotation!=inspect.Parameter.empty and annotation!=bytes: return False
        params = list(sig.parameters.values())
        if len(params)!=1: return False
        curr = params[0]
        annotation = curr.annotation
        if curr._name!='data': return False
        if curr._annotation!=inspect.Parameter.empty and annotation!=bytes: return False
        sig = inspect.signature(Compressor.flush)
        params = list(sig.parameters.values())
        annotation = sig.return_annotation
        if annotation!=inspect.Parameter.empty and annotation!=bytes: return False
        if len(params)!=0: return False

        # sig = inspect.signature(Decompressor.decompress)
        # annotation = sig.return_annotation
        # if annotation!=inspect.Parameter.empty and annotation!=bytes: return False
        # params = list(sig.parameters.values())
        # cdef cython.uchar l = len(params)
        # if l==2:
        #     curr = params[0]
        #     annotation = curr.annotation
        #     if curr._name!='maxlevel': return False
        #     if curr._annotation!=inspect.Parameter.empty and annotation!=int: return False
        # if l!=1: return False
        # curr = params[0]
        # annotation = curr.annotation
        # if curr._name!='data': return False
        # if curr._annotation!=inspect.Parameter.empty and annotation!=bytes: return False

        return True
    def __init__(self, str data, str encoding='utf-8', object lib=gzip):
        self.lib = lib
        self.data = _c_compress(lib.compress, data.encode(encoding))
        self.encoding = encoding
    @classmethod
    def from_encoded(cls, bytes data, str encoding='utf-8', object lib=gzip) -> CompressedString:
        self = cls.__new__(cls)
        self.lib = lib
        self.data = _c_compress(self.compressor, data)
        self.encoding = encoding
        return self
    @classmethod
    def from_compressed(cls, bytes data, str encoding='utf-8', object lib=gzip) -> CompressedString:
        self = cls.__new__(cls)
        self.lib = lib
        self.data = data
        self.encoding = encoding
        return self
    def __str__(self) -> str:
        return self.get()
    def __repr__(self) -> str:
        cdef object cls = self.__class__
        return f"{cls.__name__}.{cls.from_compressed.__name__}(data={self.data!r}, encoding={self.encoding!r}, lib={self.lib!r})"
    def __format__(self, object format_spec) -> str:
        return self.get().__format__(format_spec)
    cpdef void set(self, str data):
        self.data = _c_compress(self.lib.compress, data.encode(self.encoding))
    cpdef void set_encoded(self, bytes data):
        self.data = _c_compress(self.lib.compress, data)
    cpdef void set_compressed(self, bytes data):
        self.data = data
    cpdef object get_data(self): # return t.Union[bytes,memoryview]:
        """Fastest of the get methods; Returns memoryview if compression wasn't used, but bytes if compression was used"""
        return _c_decompress(self.lib.decompress, self.data)
    cpdef bytes get_bytes(self):
        res = _c_decompress(self.lib.decompress, self.data)
        return res.tobytes() if isinstance(res, memoryview) else res
    cpdef str get(self):
        cdef object decomp = _c_decompress(self.lib.decompress, self.data)
        cdef bytes res = decomp.tobytes() if isinstance(decomp, memoryview) else decomp
        return res.decode(self.encoding)
    def __add__(self, bytes other) -> CompressedString:
        cdef object compressor = self.lib._CompressorAlias_for_gllCompressedString()
        cdef object __cd = conditional_decompress
        cdef object __proc = compressor.compress
        __proc(__cd(self.data))
        __proc(__cd(other))
        return self.__class__.from_compressed(compressor.flush(), encoding=self.encoding)
    def __iadd__(self, bytes other) -> None:
        cdef object compressor = self.lib._CompressorAlias_for_gllCompressedString()
        cdef object __cd = conditional_decompress
        cdef object __proc = compressor.compress
        __proc(__cd(self.data))
        __proc(__cd(other))
        self.data = compressor.flush()
    def __mul__(self, const cython.uint other) -> CompressedString:
        cdef bytes data = conditional_decompress(self.data)
        cdef object compressor = self.lib._CompressorAlias_for_gllCompressedString()
        cdef object __compressor_compress = compressor.compress
        for _ in range(other):
            __compressor_compress(data)
        return self.__class__.from_compressed(compressor.flush(), encoding=self.encoding)
    def __imul__(self, const cython.uint other) -> None:
        cdef bytes data = conditional_decompress(self.data)
        cdef object compressor = self.lib._CompressorAlias_for_gllCompressedString()
        cdef object __compressor_compress = compressor.compress
        for _ in range(other):
            __compressor_compress(data)
        self.data = compressor.flush()
