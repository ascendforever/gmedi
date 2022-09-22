


from glite.__cimports cimport *

cdef object _c_compress(object method, object b, bytes precompressed=*, float min_savings=*)
cdef object _c_decompress(object method, object b)
cdef bytes _c_decompress_split(object method, const bint decompress, object b)
cdef tuple _c_compress_split(object method, object b, bytes precompressed=*, float min_savings=*)

cpdef object bz2_decompress_conditional(object b)
cpdef object bz2_compress_conditional(object b, bytes precompressed=*, float min_savings=*)
cpdef object bz2_decompress_conditional_split(const bint decompress, object b)
cpdef  tuple bz2_compress_conditional_split(object b, bytes precompressed=*, float min_savings=*)
cpdef object lzma_decompress_conditional(object b)
cpdef object lzma_compress_conditional(object b, bytes precompressed=*, float min_savings=*)
cpdef object lzma_decompress_conditional_split(const bint decompress, object b)
cpdef  tuple lzma_compress_conditional_split(object b, bytes precompressed=*, float min_savings=*)
cpdef object gzip_decompress_conditional(object b)
cpdef object gzip_compress_conditional(object b, bytes precompressed=*, float min_savings=*)
cpdef object gzip_decompress_conditional_split(const bint decompress, object b)
cpdef  tuple gzip_compress_conditional_split(object b, bytes precompressed=*, float min_savings=*)


cdef class CompressedString:
    cdef readonly object lib
    cdef readonly bytes data
    cdef readonly str encoding
    cpdef void set(self, str data)
    cpdef void set_encoded(self, bytes data)
    cpdef void set_compressed(self, bytes data)
    cpdef object get_data(self)
    cpdef bytes get_bytes(self)
    cpdef str get(self)
