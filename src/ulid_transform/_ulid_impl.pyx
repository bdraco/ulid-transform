# distutils: language = c++
from libcpp.string cimport string

import cython


cdef extern from "ulid_wrapper.h":
    string _cpp_ulid()
    string _cpp_ulid_at_time(double timestamp)
    string _cpp_ulid_to_bytes(string ulid)


def _ulid_now() -> str:
    return _cpp_ulid().decode("ascii")

def _ulid_at_time(time: float) -> str:
    return _cpp_ulid_at_time(time).decode("ascii")

def _ulid_to_bytes(ulid_str: str) -> bytes:
    if len(ulid_str) != 26:
        raise ValueError("ULID must be 26 characters")
    return _cpp_ulid_to_bytes(ulid_str.encode("ascii"))
