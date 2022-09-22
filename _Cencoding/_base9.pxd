








from cpython cimport int as PyInt

cpdef bytes b255encode(bytes data)
cpdef bytes b255encode_npz(bytes data)
cpdef bytes b255encode_int(PyInt data)
cdef bytes _b255encode_int(PyInt data)
cpdef bytes b255decode(object data)
cpdef bytes b255decode_npz(object data)
cpdef PyInt b255decode_int(object data)

cpdef bytes b254encode(bytes data)
cpdef bytes b254encode_npz(bytes data)
cpdef bytes b254encode_int(PyInt data)
cdef bytes _b254encode_int(PyInt data)
cpdef bytes b254decode(object data)
cpdef bytes b254decode_npz(object data)
cpdef PyInt b254decode_int(object data)

cpdef bytes b95alphabet()
cpdef bytes b95encode(bytes data)
cpdef bytes b95encode_npz(bytes data)
cpdef bytes b95encode_int(PyInt data)
cdef bytes _b95encode_int(PyInt data)
cpdef bytes b95decode(object data)
cpdef bytes b95decode_npz(object data)
cpdef PyInt b95decode_int(object data)

cpdef bytes b94alphabet()
cpdef bytes b94encode(bytes data)
cpdef bytes b94encode_npz(bytes data)
cpdef bytes b94encode_int(PyInt data)
cdef bytes _b94encode_int(PyInt data)
cpdef bytes b94decode(object data)
cpdef bytes b94decode_npz(object data)
cpdef PyInt b94decode_int(object data)

cpdef bytes b93alphabet()
cpdef bytes b93encode(bytes data)
cpdef bytes b93encode_npz(bytes data)
cpdef bytes b93encode_int(PyInt data)
cdef bytes _b93encode_int(PyInt data)
cpdef bytes b93decode(object data)
cpdef bytes b93decode_npz(object data)
cpdef PyInt b93decode_int(object data)

cpdef bytes b92alphabet()
cpdef bytes b92encode(bytes data)
cpdef bytes b92encode_npz(bytes data)
cpdef bytes b92encode_int(PyInt data)
cdef bytes _b92encode_int(PyInt data)
cpdef bytes b92decode(object data)
cpdef bytes b92decode_npz(object data)
cpdef PyInt b92decode_int(object data)

cpdef bytes b91alphabet()
cpdef bytes b91encode(bytes data)
cpdef bytes b91encode_npz(bytes data)
cpdef bytes b91encode_int(PyInt data)
cpdef bytes b91encode_int_barray(PyInt data)
cdef bytes _b91encode_int(PyInt data)
cpdef bytes b91decode(object data)
cpdef bytes b91decode_npz(object data)
cpdef PyInt b91decode_int(object data)


