# distutils: language = c++
from libcpp.string cimport string


cdef extern from "ulid_wrapper.h":
    string _cpp_ulid()
    string _cpp_ulid_at_time(double timestamp)
    bytes _cpp_ulid_to_bytes(string ulid)


def _ulid_now() -> str:
    ulid_bytes = _cpp_ulid()
    return ulid_bytes.decode("utf-8")


def _ulid_at_time(time: float) -> str:
    ulid_bytes = _cpp_ulid_at_time(time)
    return ulid_bytes.decode("utf-8")

def _ulid_to_bytes(ulid: str) -> bytes:
    return _cpp_ulid_to_bytes(ulid)
