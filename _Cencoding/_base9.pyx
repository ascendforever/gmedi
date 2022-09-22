
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
    'b91encode_int_barray',
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
from glite.__cimports cimport *

# cimport cython
# from cpython cimport int as PyInt
from cpython cimport array


cpdef bytes b255encode(bytes data):
    return _b255encode_int(int.from_bytes(b'\x01' + data, 'big', signed=False))
cpdef bytes b255encode_npz(bytes data):
    return _b255encode_int(int.from_bytes(data, 'big', signed=False))
cpdef bytes b255encode_int(PyInt data): # data:pyint
    if data < 0: raise ValueError("Signed integers not allowed")
    return _b255encode_int(data)
cdef inline bytes _b255encode_int(PyInt data): # data:pyint
    cdef list enc = [] # of cython.uchar
    cdef cython.uchar mod
    __enc_append = enc.append
    while True:
        data,mod = divmod(data, 255)
        __enc_append(mod+1)
        if data==0: break
    return bytes(enc)
cpdef bytes b255decode(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b255decode_int(data))[1:]
cpdef bytes b255decode_npz(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b255decode_int(data))
cpdef PyInt b255decode_int(object data): # data:col.abc.Reversible[cython.uchar] # return pyint
    cdef PyInt dec = 0 # pyint
    cdef cython.uchar x
    for x in reversed(data):
        dec = 255*dec + x-1
    return dec


cpdef bytes b254encode(bytes data):
    return _b254encode_int(int.from_bytes(b'\x01' + data, 'big', signed=False))
cpdef bytes b254encode_npz(bytes data):
    return _b254encode_int(int.from_bytes(data, 'big', signed=False))
cpdef bytes b254encode_int(PyInt data): # data:pyint
    if data < 0: raise ValueError("Signed integers not allowed")
    return _b254encode_int(data)
cdef inline bytes _b254encode_int(PyInt data): # data:pyint
    cdef list enc = [] # of cython.uchar
    cdef cython.uchar mod
    __enc_append = enc.append
    while True:
        data,mod = divmod(data, 254)
        __enc_append(mod+2)
        if data==0: break
    return bytes(enc)
cpdef bytes b254decode(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b254decode_int(data))[1:]
cpdef bytes b254decode_npz(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b254decode_int(data))
cpdef PyInt b254decode_int(object data): # data:col.abc.Reversible[cython.uchar] # return pyint
    cdef PyInt dec = 0 # pyint
    cdef cython.uchar x
    for x in reversed(data):
        dec = 254*dec + x-2
    return dec


_b95_alphabet = None
cpdef bytes b95alphabet():
    global _b95_alphabet
    if _b95_alphabet is None:
        _b95_alphabet = b' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    return _b95_alphabet
cpdef bytes b95encode(bytes data):
    return _b95encode_int(int.from_bytes(b'\x01' + data, 'big', signed=False))
cpdef bytes b95encode_npz(bytes data):
    return _b95encode_int(int.from_bytes(data, 'big', signed=False))
cpdef bytes b95encode_int(PyInt data): # data:pyint
    if data < 0: raise ValueError("Signed integers not allowed")
    return _b95encode_int(data)
cdef inline bytes _b95encode_int(PyInt data): # data:pyint
    cdef list enc = [] # of cython.uchar
    cdef cython.uchar mod
    __enc_append = enc.append
    while True:
        data,mod = divmod(data, 95)
        __enc_append(mod+32)
        if data==0: break
    return bytes(enc)
cpdef bytes b95decode(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b95decode_int(data))[1:]
cpdef bytes b95decode_npz(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b95decode_int(data))
cpdef PyInt b95decode_int(object data): # data:col.abc.Reversible[cython.uchar] # return pyint
    cdef PyInt dec = 0 # pyint
    cdef cython.uchar x
    for x in reversed(data):
        dec = 95*dec + x-32
    return dec


_b94_alphabet = None
cpdef bytes b94alphabet():
    global _b94_alphabet
    if _b94_alphabet is None:
        _b94_alphabet = b'!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    return _b94_alphabet
cpdef bytes b94encode(bytes data):
    return _b94encode_int(int.from_bytes(b'\x01' + data, 'big', signed=False))
cpdef bytes b94encode_npz(bytes data):
    return _b94encode_int(int.from_bytes(data, 'big', signed=False))
cpdef bytes b94encode_int(PyInt data): # data:pyint
    if data < 0: raise ValueError("Signed integers not allowed")
    return _b94encode_int(data)
cdef inline bytes _b94encode_int(PyInt data): # data:pyint
    cdef list enc = [] # of cython.uchar
    cdef cython.uchar mod
    __enc_append = enc.append
    while True:
        data,mod = divmod(data, 94)
        __enc_append(mod+33)
        if data==0: break
    return bytes(enc)
cpdef bytes b94decode(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b94decode_int(data))[1:]
cpdef bytes b94decode_npz(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b94decode_int(data))
cpdef PyInt b94decode_int(object data): # return pyint # data:col.abc.Reversible[cython.uchar]
    cdef PyInt dec = 0 # pyint
    cdef cython.uchar x
    for x in reversed(data):
        dec = 94*dec + x-33
    return dec

_b93_alphabet = None
cpdef bytes b93alphabet():
    global _b93_alphabet
    if _b93_alphabet is None:
        _b93_alphabet = b'!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_abcdefghijklmnopqrstuvwxyz{|}~'
    return _b93_alphabet
cpdef bytes b93encode(bytes data):
    return _b93encode_int(int.from_bytes(b'\x01' + data, 'big', signed=False))
cpdef bytes b93encode_npz(bytes data):
    return _b93encode_int(int.from_bytes(data, 'big', signed=False))
cpdef bytes b93encode_int(PyInt data): # data:pyint
    if data < 0: raise ValueError("Signed integers not allowed")
    return _b93encode_int(data)
cdef inline bytes _b93encode_int(PyInt data): # data:pyint
    cdef list enc = [] # of cython.uchar
    cdef cython.uchar mod
    __enc_append = enc.append
    while True:
        data,mod = divmod(data, 93)
        #                        `=96-33=63
        __enc_append(mod + (34 if mod >= 63 else 33))
        if data==0: break
    return bytes(enc)
cpdef bytes b93decode(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b93decode_int(data))[1:]
cpdef bytes b93decode_npz(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b93decode_int(data))
cpdef PyInt b93decode_int(object data): # data:col.abc.Reversible[cython.uchar] # returns pyint
    cdef PyInt dec = 0 # pyint
    cdef cython.uchar x
    for x in reversed(data):
        #                            `=96
        dec = 93*dec + x - (34 if x >= 96 else 33)
    return dec

_b92_alphabet = None
cpdef bytes b92alphabet():
    global _b92_alphabet
    if _b92_alphabet is None:
        _b92_alphabet = b'!#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_abcdefghijklmnopqrstuvwxyz{|}~'
    return _b92_alphabet
cpdef bytes b92encode(bytes data):
    return _b92encode_int(int.from_bytes(b'\x01' + data, 'big', signed=False))
cpdef bytes b92encode_npz(bytes data):
    return _b92encode_int(int.from_bytes(data, 'big', signed=False))
cpdef bytes b92encode_int(PyInt data): # data:pyint
    if data < 0: raise ValueError("Signed integers not allowed")
    return _b92encode_int(data)
cdef inline bytes _b92encode_int(PyInt data): # data:pyint
    cdef list enc = [] # of cython.uchar
    cdef cython.uchar mod
    __enc_append = enc.append
    while True:
        data,mod = divmod(data, 92)
        #                    `=96-33-1=62          "=34-33=1
        __enc_append(mod + (35 if mod >= 62 else (34 if mod >= 1 else 33))) # ` = 96; 96-34 = 62 # skip `
        if data==0: break
    return bytes(enc)
cpdef bytes b92decode(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b92decode_int(data))[1:]
cpdef bytes b92decode_npz(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b92decode_int(data))
cpdef PyInt b92decode_int(object data): # data:col.abc.Reversible[cython.uchar] # returns pyint
    cdef PyInt dec = 0 # pyint
    cdef cython.uchar x
    for x in reversed(data):
        #                            `=96                "=34
        dec = 92*dec + x - (35 if x >= 96 else (34 if x >= 34 else 33))
    return dec

_b91_alphabet = None
cpdef bytes b91alphabet():
    global _b91_alphabet
    if _b91_alphabet is None:
        _b91_alphabet = b'!#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}~'
    return _b91_alphabet
cpdef bytes b91encode(bytes data):
    return _b91encode_int(int.from_bytes(b'\x01' + data, 'big', signed=False))
cpdef bytes b91encode_npz(bytes data):
    return _b91encode_int(int.from_bytes(data, 'big', signed=False))
cpdef bytes b91encode_int(PyInt data): # data:pyint
    if data < 0: raise ValueError("Signed integers not allowed")
    return _b91encode_int(data)
cpdef bytes b91encode_int_barray(PyInt data): # data:pyint
    if data < 0: raise ValueError("Signed integers not allowed")
    return _b91encode_int_barr(data)
cdef inline bytes _b91encode_int(PyInt data): # data:pyint
    cdef list enc = [] # of cython.uchar
    cdef cython.uchar mod
    __enc_append = enc.append
    while True:
        data,mod = divmod(data, 91)
        #                    `=96-33-2=61          \=92-33-1=58          "=34-33=1
        __enc_append(mod + (36 if mod >= 61 else (35 if mod >= 58 else (34 if mod >= 1 else 33))))
        if data==0: break
    return bytes(enc)
# from cpython.bytearray cimport PyByteArray_AsString
# from cpython.bytes cimport PyBytes_FromString
cdef inline bytes _b91encode_int_barr(PyInt data): # data:pyint
    cdef cython.uchar i, mod
    cdef cython.uchar am = math.ceil(math.log(data, 91))
    cdef bytearray enc = bytearray(am)
    # cdef cython.uchar[:] view = enc
    for i in range(am):
        data,mod = divmod(data, 91)
        #                    `=96-33-2=61          \=92-33-1=58          "=34-33=1
        enc[i] = mod + (36 if mod >= 61 else (35 if mod >= 58 else (34 if mod >= 1 else 33)))
    return bytes(enc) # WTF ITS LITERALLY FASTER TO MAKE IT BYTES ???
cpdef bytes b91decode(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b91decode_int(data))[1:]
cpdef bytes b91decode_npz(object data): # data:col.abc.Reversible[cython.uchar]
    return upy_to_bytes(b91decode_int(data))
cpdef PyInt b91decode_int(object data): # data:col.abc.Reversible[cython.uchar] # returns pyint
    cdef PyInt dec = 0 # pyint
    cdef cython.uchar x
    for x in reversed(data):
        #                            `=96                \=92                "=34
        dec = 91*dec + x - (36 if x >= 96 else (35 if x >= 92 else (34 if x >= 34 else 33)))
    return dec

def custom_encoding(object exclusions) -> tuple: # exclusions:col.abc.Sequence[cython.uchar]
    for exc in exclusions:
        if 33 > exc > 126:
            raise ValueError(f"Out of bounds ascii character: {exc}")
    cdef array.array exclusions_arr = array.array('B', sorted(exclusions, reverse=True)) # of cython.uchar
    cdef frozenset __fse = frozenset(exclusions_arr)
    cdef cython.uchar __le = len(exclusions_arr)
    # yes using this big bytestring is faster than bytes([i for i in range(33, 126+1)])
    cdef cython.uchar option_count = sum(1 for x in b'!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~' if x not in __fse)
    # this = exclusion - 33 - level - 1
    cdef array.array exclusions_minied = array.array('B', [exc - k  for k,exc in zip(range(__le+32, 32, -1), exclusions_arr)])
    cdef array.array exclusion_levels = array.array('B', range(__le+33, 33, -1))
    def encode(bytes data) -> bytes:
        return _encode_int(int.from_bytes(data, 'big', signed=False))
    def encode_int(object data) -> bytes: # data:pyint
        if data < 0: raise ValueError("Signed integers not allowed")
        return _encode_int(data)
    def _encode_int(object data) -> bytes: # data:pyint
        cdef list enc = [] # of cython.uchar
        __append = enc.append
        cdef cython.uchar mod
        while True:
            data,mod = divmod(data, option_count)
            for l,excm in zip(exclusion_levels, exclusions_minied):
                if mod >= excm:
                    __append(mod + l)
                    break
            else:
                __append(mod + 33)
            if data==0:
                break
        return bytes(enc)
    def decode(object data) -> bytes: # data:col.abc.Reversible
        return upy_to_bytes(decode_int(data))
    def decode_int(object data) -> object: # data:col.abc.Reversible # return pyint
        dec:cython.ulonglong = 0
        x:cython.uchar
        for x in reversed(data):
            for l,exc in zip(exclusion_levels, exclusions_arr):
                if x >= exc:
                    dec = option_count*dec + x - l
                    break
            else:
                dec = option_count*dec + x - 33
        return dec
    return encode,encode_int,decode,decode_int



from binascii import b2a_base64, a2b_base64
from base64 import _urlsafe_encode_translation as b64_urlsafe_encode_translation, _urlsafe_decode_translation as b64_urlsafe_decode_translation, _bytes_from_decode_data as b64_bytes_from_decode_data

cpdef bytes b64encode(bytes s):
    return b2a_base64(s, newline=False)
cpdef bytes b64decode(object s): # str or bytes as input
    return a2b_base64(b64_bytes_from_decode_data(s))

cpdef bytes urlsafe_b64encode(bytes s):
    return b2a_base64(s, newline=False).translate(b64_urlsafe_encode_translation)
cpdef bytes urlsafe_b64decode(object s): # str or bytes as input
    return a2b_base64(b64_bytes_from_decode_data(s).translate(b64_urlsafe_decode_translation))
