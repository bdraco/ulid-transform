# distutils: language = c++
from libcpp.string cimport string


cdef extern from "ulid_wrapper.h":
    string _gen_ulid()
    string _gen_ulid_at_time(double timestamp)


def _ulid_now() -> str:
    ulid_bytes = _gen_ulid()
    return ulid_bytes.decode("utf-8")


def _ulid_at_time(time: float) -> str:
    ulid_bytes = _gen_ulid_at_time(time)
    return ulid_bytes.decode("utf-8")
