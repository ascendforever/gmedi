
__all__ = [
    'b255encode',
    'b255encode_npz',
    'b255encode_int',
    'b255decode',
    'b255decode_npz',
    'b255decode_int',

    'b254encode',
    'b254encode_npz',
    'b254encode_int',
    'b254decode',
    'b254decode_npz',
    'b254decode_int',

    'b95alphabet',
    'b95encode',
    'b95encode_npz',
    'b95encode_int',
    'b95decode',
    'b95decode_npz',
    'b95decode_int',

    'b94alphabet',
    'b94encode',
    'b94encode_npz',
    'b94encode_int',
    'b94decode',
    'b94decode_npz',
    'b94decode_int',

    'b93alphabet',
    'b93encode',
    'b93encode_npz',
    'b93encode_int',
    'b93decode',
    'b93decode_npz',
    'b93decode_int',

    'b92alphabet',
    'b92encode',
    'b92encode_npz',
    'b92encode_int',
    'b92decode',
    'b92decode_npz',
    'b92decode_int',

    'b91alphabet',
    'b91encode',
    'b91encode_npz',
    'b91encode_int',
    # 'b91encode_int_barray',
    'b91decode',
    'b91decode_npz',
    'b91decode_int',

    'custom_encoding',

    'b64encode',
    'b64decode',
    'urlsafe_b64encode',
    'urlsafe_b64decode',
]

from gmedi.__common import *
from gmedi.__static import *


def b255encode(data:bytes) -> bytes:
    r"""Encode data in base 255 (custom format) - alphabet contains all ascii characters \x00
    [Created 2/12/22]"""
def b255encode_npz(data:bytes) -> bytes:
    """Use if data is gurranteed to have NPZ - no preceding zeros
    [Created 2/12/22]"""
def b255encode_int(data:int) -> bytes:
    """Encodes unsigned integer (faster)
    [Created 2/12/22]"""
def b255decode(data:abcs.Reversible[int]) -> bytes:
    """[Created 2/12/22]"""
def b255decode_npz(data:abcs.Reversible[int]) -> bytes:
    """Use if unencoded data is gurranteed to have NPZ - no preceding zeros
    [Created 2/12/22]"""
def b255decode_int(data:abcs.Reversible[int]) -> int:
    """Returns unsigned integer (faster)
    [Created 2/12/22]"""


def b254encode(data:bytes) -> bytes:
    r"""Encode data in base 254 (custom format) - alphabet contains all ascii characters \x00 and \x01
    [Created 2/12/22]"""
def b254encode_npz(data:bytes) -> bytes:
    """Use if data is gurranteed to have NPZ - no preceding zeros
    [Created 2/12/22]"""
def b254encode_int(data:int) -> bytes:
    """Encodes unsigned integer (faster)
    [Created 2/12/22]"""
def b254decode(data:abcs.Reversible[int]) -> bytes:
    """[Created 2/12/22]"""
def b254decode_npz(data:abcs.Reversible[int]) -> bytes:
    """Use if unencoded data is gurranteed to have NPZ - no preceding zeros
    [Created 2/12/22]"""
def b254decode_int(data:abcs.Reversible[int]) -> int:
    """Returns unsigned integer (faster)
    [Created 2/12/22]"""


def b95alphabet() -> bytes:
    """Ascii 32-126 inclusive"""
    return b' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
def b95encode(data:bytes) -> bytes:
    """Encode data in base 95 (custom format) - alphabet contains all ascii characters except for control characters
    [Created 1/7/22]"""
def b95encode_npz(data:bytes) -> bytes:
    """Use if data is gurranteed to have NPZ - no preceding zeros
    [Created 1/12/22]"""
def b95encode_int(data:int) -> bytes:
    """Encodes unsigned integer (faster)
    [Created 1/7/22]"""
def b95decode(data:abcs.Reversible[int]) -> bytes:
    """[Created 1/7/22]"""
def b95decode_npz(data:abcs.Reversible[int]) -> bytes:
    """Use if unencoded data is gurranteed to have NPZ - no preceding zeros
    [Created 1/12/22]"""
def b95decode_int(data:abcs.Reversible[int]) -> int:
    """Returns unsigned integer (faster)
    [Created 1/7/22]"""


def b94alphabet() -> bytes:
    """Ascii 33-126 inclusive"""
    return b'!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
def b94encode(data:bytes) -> bytes:
    """Encode data in base 94 (custom format) - alphabet contains all ascii characters except for space and control characters
    [Created 12/7/21]"""
def b94encode_npz(data:bytes) -> bytes:
    """Use if data is gurranteed to have NPZ - no preceding zeros
    [Created 1/12/22]"""
def b94encode_int(data:int) -> bytes:
    """Encodes unsigned integer (faster)
    [Created 12/10/21]"""
def b94decode(data:abcs.Reversible[int]) -> bytes:
    """[Created 12/7/21]"""
def b94decode_npz(data:abcs.Reversible[int]) -> bytes:
    """Use if unencoded data is gurranteed to have NPZ - no preceding zeros
    [Created 1/12/22]"""
def b94decode_int(data:abcs.Reversible[int]) -> int:
    """Returns unsigned integer (faster)
    [Created 12/7/21]"""

def b93alphabet() -> bytes:
    """Ascii 33-126 inclusive, excluding 96 = `"""
    return b'!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_abcdefghijklmnopqrstuvwxyz{|}~'
def b93encode(data:bytes) -> bytes:
    """Encode data in base 93 (custom format) - alphabet contains all ascii characters except for space, `, and control characters
    [Created 12/8/21]"""
def b93encode_npz(data:bytes) -> bytes:
    """Use if data is gurranteed to have NPZ - no preceding zeros
    [Created 1/12/22]"""
def b93encode_int(data:int) -> bytes:
    """Encodes unsigned integer (faster)
    [Created 12/10/21]"""
def b93decode(data:abcs.Reversible[int]) -> bytes:
    """[Created 12/8/21]"""
def b93decode_npz(data:abcs.Reversible[int]) -> bytes:
    """Use if unencoded data is gurranteed to have NPZ - no preceding zeros
    [Created 1/12/22]"""
def b93decode_int(data:abcs.Reversible[int]) -> int:
    """Returns unsigned integer (faster)
    [Created 12/8/21]"""

def b92alphabet() -> bytes:
    """Ascii 33-126 inclusive, excluding 34 = " and 96 = `"""
    return b'!#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_abcdefghijklmnopqrstuvwxyz{|}~'
def b92encode(data:bytes) -> bytes:
    """Encode data in base 92 (custom format) - alphabet contains all ascii characters except for space, `, !, and control characters
    [Created 12/10/21]"""
def b92encode_npz(data:bytes) -> bytes:
    """Use if data is gurranteed to have NPZ - no preceding zeros
    [Created 1/12/22]"""
def b92encode_int(data:int) -> bytes:
    """Encodes unsigned integer (faster)
    [Created 12/10/21]"""
def b92decode(data:abcs.Reversible[int]) -> bytes:
    """[Created 12/10/21]"""
def b92decode_npz(data:abcs.Reversible[int]) -> bytes:
    """Use if unencoded data is gurranteed to have NPZ - no preceding zeros
    [Created 1/12/22]"""
def b92decode_int(data:abcs.Reversible[int]) -> int:
    """Returns unsigned integer (faster)
    [Created 12/10/21]"""

def b91alphabet() -> bytes:
    """Ascii 33-126 inclusive, excluding 34 = " and 96 = ` and 92 = \\"""
    return b'!#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}~'
def b91encode(data:bytes) -> bytes:
    """Encode data in base 91 (custom format) - alphabet contains all ascii characters except for space, `, !, and control characters
    [Created 12/29/21]"""
def b91encode_npz(data:bytes) -> bytes:
    """Use if data is gurranteed to have NPZ - no preceding zeros
    [Created 1/12/22]"""
def b91encode_int(data:int) -> bytes:
    """Encodes unsigned integer (faster)
    [Created 12/29/21]"""
def b91decode(data:abcs.Reversible[int]) -> bytes:
    """[Created 12/29/21]"""
def b91decode_npz(data:abcs.Reversible[int]) -> bytes:
    """Use if unencoded data is gurranteed to have NPZ - no preceding zeros
    [Created 1/12/22]"""
def b91decode_int(data:abcs.Reversible[int]) -> int:
    """Returns unsigned integer (faster)
    [Created 12/29/21]"""

def custom_encoding(exclusions:abcs.Sequence[int]) -> tuple:
    """Returns encoding, encoding-int, decoding, decoding-int functions that utilize Ascii 33-126 inclusive, excluding those passed as `exclusions`
    This includes every ascii character except space
    Use prebuilts over this, as the resulting functions are slower quite a bit (due to the fact that they are not cython cpdef function, just regular def functions)
    [Created 12/29/21]"""
    def encode(data:bytes) -> bytes: ...
    def encode_int(data:int) -> bytes: ...
    def decode(data:abcs.Reversible[int]) -> bytes: ...
    def decode_int(data:abcs.Reversible[int]) -> int: ...
    return encode,encode_int,decode,decode_int


def b64encode(s:bytes) -> bytes:
    """Faster than base64.b64encode as it cuts out useless code in its implementation
    [Created 6/27/22]"""
def b64decode(s:bytes|str) -> bytes:
    """Faster than base64.b64decode as it cuts out useless code in its implementation
    [Created 6/27/22]"""

def urlsafe_b64encode(s:bytes) -> bytes:
    """Faster than base64.urlsafe_b64encode as it cuts out useless code in its implementation
    [Created 6/27/22]"""
def urlsafe_b64decode(s:bytes|str) -> bytes:
    """Faster than base64.urlsafe_b64decode as it cuts out useless code in its implementation
    [Created 6/27/22]"""
