from __future__ import annotations


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

# noinspection PyUnusedLocal
def bz2_decompress_conditional(b:bytes|memoryview) -> bytes|memoryview:
    """If the first byte is `0`, returns unchanged memory ([1:])
    If the first bytes is `1`, returns decompressed memory ([1:])
    [Created 8/29/21 // remade 1/3/22]"""
# noinspection PyUnusedLocal
def bz2_compress_conditional(b:bytes|memoryview, precompressed:None|bytes=None, min_savings:float=0.10) -> bytes:
    """If the bytes are larger than the compressed*(1+min_savings), prepend bytes `1`, else prepend bytes `0`
    if `compressed` is `None`, compress `b`
    [Created 8/29/21 // remade 1/3/22]"""
# noinspection PyUnusedLocal
def bz2_decompress_conditional_split(decompress:bool, b:bytes|memoryview) -> bytes:
    """If the first byte is `0`, returns unchanged memory ([1:])
    If the first bytes is `1`, returns decompressed memory ([1:])
    [Created 8/29/21 // remade 1/3/22]"""
# noinspection PyUnusedLocal
def bz2_compress_conditional_split(b:bytes|memoryview, precompressed:None|bytes=None, min_savings:float=0.10) -> tuple[bool,bytes]:
    """If the bytes are larger than the compressed*(1+min_savings), prepend bytes `1`, else prepend bytes `0`
    if `compressed` is `None`, compress `b`
    [Created 8/29/21 // remade 1/3/22]"""
# noinspection PyUnusedLocal
def lzma_decompress_conditional(b:bytes|memoryview) -> bytes|memoryview:
    """If the first byte is `0`, returns unchanged memory ([1:])
    If the first bytes is `1`, returns decompressed memory ([1:])
    [Created 8/29/21 // remade 1/3/22]"""
# noinspection PyUnusedLocal
def lzma_compress_conditional(b:bytes|memoryview, precompressed:None|bytes=None, min_savings:float=0.10) -> bytes:
    """If the bytes are larger than the compressed*(1+min_savings), prepend bytes `1`, else prepend bytes `0`
    if `compressed` is `None`, compress `b`
    [Created 8/29/21 // remade 1/3/22]"""
# noinspection PyUnusedLocal
def lzma_decompress_conditional_split(decompress:bool, b:bytes|memoryview) -> bytes:
    """If the first byte is `0`, returns unchanged memory ([1:])
    If the first bytes is `1`, returns decompressed memory ([1:])
    [Created 8/29/21 // remade 1/3/22]"""
# noinspection PyUnusedLocal
def lzma_compress_conditional_split(b:bytes|memoryview, precompressed:None|bytes=None, min_savings:float=0.10) -> tuple[bool,bytes]:
    """If the bytes are larger than the compressed*(1+min_savings), prepend bytes `1`, else prepend bytes `0`
    if `compressed` is `None`, compress `b`
    [Created 8/29/21 // remade 1/3/22]"""
# noinspection PyUnusedLocal
def gzip_decompress_conditional(b:bytes|memoryview) -> bytes|memoryview:
    """If the first byte is `0`, returns unchanged memory ([1:])
    If the first bytes is `1`, returns decompressed memory ([1:])
    [Created 8/29/21 // remade 1/3/22]"""
# noinspection PyUnusedLocal
def gzip_compress_conditional(b:bytes|memoryview, precompressed:None|bytes=None, min_savings:float=0.10) -> bytes:
    """If the bytes are larger than the compressed*(1+min_savings), prepend bytes `1`, else prepend bytes `0`
    if `compressed` is `None`, compress `b`
    [Created 8/29/21 // remade 1/3/22]"""
# noinspection PyUnusedLocal
def gzip_decompress_conditional_split(decompress:bool, b:bytes|memoryview) -> bytes:
    """If the first byte is `0`, returns unchanged memory ([1:])
    If the first bytes is `1`, returns decompressed memory ([1:])
    [Created 8/29/21 // remade 1/3/22]"""
# noinspection PyUnusedLocal
def gzip_compress_conditional_split(b:bytes|memoryview, precompressed:None|bytes=None, min_savings:float=0.10) -> tuple[bool,bytes]:
    """If the bytes are larger than the compressed*(1+min_savings), prepend bytes `1`, else prepend bytes `0`
    if `compressed` is `None`, compress `b`
    [Created 8/29/21 // remade 1/3/22]"""

class CompressedString:
    """GZIP/BZ2/LZMA compressed string (can be other compression types; defaults to gzip)
    It is recommended to use gzip with string sizes below around 64 or 128 kilobytes
    To use other methods, pass `lib` when creating instance
    `lib` should be an object (likely a module) containing 3 object: a `compress` function `decompress` function and `XYZCompressor` class
    The `XYZCompressor` can have any regex `a-zA-Z_` characters before `Compressor`
    This class should also have a `compress` function and a `flush` function
    All function signatures will be checked
    Use the .supports_lib classmethod to test if a lib is supported"""
    __slots__ = ('lib', 'data', 'encoding')
    @classmethod
    def supports_lib(cls, lib:object) -> bool: ...
    # noinspection PyUnusedLocal
    def __init__(self, data:str, encoding:str='utf-8', lib=gzip):
        self.lib:t.Final = [gzip, bz2, lzma][0]
        self.data:t.Final[bytes] = bytes(1)
        self.encoding:t.Final[str] = encoding
    # noinspection PyUnusedLocal
    @classmethod
    def from_encoded(cls, data:bytes, encoding:str= 'utf-8', lib=gzip) -> CompressedString: ...
    # noinspection PyUnusedLocal
    @classmethod
    def from_compressed(cls, data:bytes, encoding:str='utf-8', lib=gzip) -> CompressedString: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __format__(self, format_spec): ...
    def set(self, data:str) -> None: ...
    def set_encoded(self, data:bytes) -> None: ...
    def set_compressed(self, data:bytes) -> None: ...
    def get_data(self) -> bytes|memoryview:
        """Fastest of the get methods; Returns memoryview if compression wasn't used, but bytes if compression was used"""
    def get_bytes(self) -> bytes:
        """Same as `res.tobytes() if isinstance((res:=self.get_data()), memoryview) else res`"""
    def get(self) -> str:
        """Same as self.get_bytes().decode(self.encoding)"""
    def __add__(self, other:bytes) -> CompressedString: ...
    def __iadd__(self, other:bytes) -> None: ...
    def __mul__(self, other:int) -> CompressedString: ...
    def __imul__(self, other:int) -> None: ...
