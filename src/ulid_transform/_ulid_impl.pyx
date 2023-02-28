# distutils: language = c++

cdef extern from "ulid_wrapper.h":
    str _ulid()



def _generate_ulid() -> str:
    return _ulid()
