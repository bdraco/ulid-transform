# distutils: language = c++
from libcpp.string cimport string
from libcpp.vector cimport vector

from typing import Optional


cdef extern from "ulid_wrapper.h":
    string _cpp_ulid_at_time(double timestamp)
    vector[unsigned char] _cpp_ulid_at_time_bytes(double timestamp)
    string _cpp_ulid_to_bytes(const char * ulid_string)
    string _cpp_ulid()
    vector[unsigned char] _cpp_ulid_bytes()
    string _cpp_bytes_to_ulid(string ulid_bytes)

def _ulid_now_bytes() -> bytes:
    return bytes(_cpp_ulid_bytes())

def _ulid_at_time_bytes(_time: float) -> bytes:
    return bytes(_cpp_ulid_at_time_bytes(_time))

def _ulid_now() -> str:
    return _cpp_ulid().decode("ascii")

def _ulid_at_time(_time: float) -> str:
    return _cpp_ulid_at_time(_time).decode("ascii")

def _ulid_to_bytes(ulid_str: str) -> bytes:
    if len(ulid_str) != 26:
        raise ValueError(f"ULID must be a 26 character string: {ulid_str}")
    return _cpp_ulid_to_bytes(ulid_str.encode("ascii"))

def _bytes_to_ulid(ulid_bytes: bytes) -> str:
    if len(ulid_bytes) != 16:
        raise ValueError(f"ULID bytes must be 16 bytes: {ulid_bytes!r}")
    return _cpp_bytes_to_ulid(ulid_bytes).decode("ascii")

def _ulid_to_bytes_or_none(ulid_str: Optional[str]) -> Optional[bytes]:
    if ulid_str is None or len(ulid_str) != 26:
        return None
    return _cpp_ulid_to_bytes(ulid_str.encode("ascii"))

def _bytes_to_ulid_or_none(ulid_bytes: Optional[bytes]) -> Optional[str]:
    if ulid_bytes is None or len(ulid_bytes) != 16:
        return None
    return _cpp_bytes_to_ulid(ulid_bytes).decode("ascii")
