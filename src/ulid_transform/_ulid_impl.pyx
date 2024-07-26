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


def ulid_hex() -> str:
    """Generate a ULID in lowercase hex that will work for a UUID.

    This ulid should not be used for cryptographically secure
    operations.

    This string can be converted with https://github.com/ahawker/ulid

    ulid.from_uuid(uuid.UUID(ulid_hex))
    """
    return bytes(_cpp_ulid_bytes()).hex()


def ulid_now_bytes() -> bytes:
    """Generate an ULID as 16 bytes that will work for a UUID."""
    return bytes(_cpp_ulid_bytes())


def ulid_at_time_bytes(timestamp: float) -> bytes:
    """Generate an ULID as 16 bytes that will work for a UUID.

    uuid.UUID(bytes=ulid_bytes)
    """
    return bytes(_cpp_ulid_at_time_bytes(timestamp))


def ulid_now() -> str:
    """Generate a ULID."""
    return _cpp_ulid().decode("ascii")


def ulid_at_time(timestamp: float) -> str:
    """Generate a ULID.

    This ulid should not be used for cryptographically secure
    operations.

     01AN4Z07BY      79KA1307SR9X4MV3
    |----------|    |----------------|
     Timestamp          Randomness
       48bits             80bits

    This string can be loaded directly with https://github.com/ahawker/ulid

    import ulid_transform as ulid_util
    import ulid
    ulid.parse(ulid_util.ulid())
    """
    return _cpp_ulid_at_time(timestamp).decode("ascii")


def ulid_to_bytes(value: str) -> bytes:
    """Decode a ulid to bytes."""
    if len(value) != 26:
        raise ValueError(f"ULID must be a 26 character string: {value}")
    return _cpp_ulid_to_bytes(value.encode("ascii"))


def bytes_to_ulid(value: bytes) -> str:
    """Encode bytes to a ulid."""
    if len(value) != 16:
        raise ValueError(f"ULID bytes must be 16 bytes: {value!r}")
    return _cpp_bytes_to_ulid(value).decode("ascii")


def ulid_to_bytes_or_none(ulid: Optional[str]) -> Optional[bytes]:
    """Convert an ulid to bytes."""
    if ulid is None or len(ulid) != 26:
        return None
    return _cpp_ulid_to_bytes(ulid.encode("ascii"))


def bytes_to_ulid_or_none(ulid_bytes: Optional[bytes]) -> Optional[str]:
    """Convert bytes to a ulid."""
    if ulid_bytes is None or len(ulid_bytes) != 16:
        return None
    return _cpp_bytes_to_ulid(ulid_bytes).decode("ascii")
