from random import getrandbits
from time import time

_ENCODE = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"

_float = float


def ulid_hex() -> str:
    """Generate a ULID in lowercase hex that will work for a UUID.

    This ulid should not be used for cryptographically secure
    operations.

    This string can be converted with https://github.com/ahawker/ulid

    ulid.from_uuid(uuid.UUID(ulid_hex))
    """
    return f"{int(time()*1000):012x}{getrandbits(80):020x}"


def ulid(timestamp: float | None = None) -> str:
    """Generate a ULID.

    This ulid should not be used for cryptographically secure
    operations.

     01AN4Z07BY      79KA1307SR9X4MV3
    |----------|    |----------------|
     Timestamp          Randomness
       48bits             80bits

    This string can be loaded directly with https://github.com/ahawker/ulid

    import homeassistant.util.ulid as ulid_util
    import ulid
    ulid.parse(ulid_util.ulid())
    """
    return _ulid(timestamp or time())


def _ulid(timestamp: _float) -> str:
    ulid_bytes = int((timestamp) * 1000).to_bytes(6, byteorder="big") + int(
        getrandbits(80)
    ).to_bytes(10, byteorder="big")

    # This is base32 crockford encoding with the loop unrolled for performance
    #
    # This code is adapted from:
    # https://github.com/ahawker/ulid/blob/06289583e9de4286b4d80b4ad000d137816502ca/ulid/base32.py#L102
    #
    ulid_bytes0 = ulid_bytes[0]
    ulid_bytes1 = ulid_bytes[1]
    ulid_bytes2 = ulid_bytes[2]
    ulid_bytes3 = ulid_bytes[3]
    ulid_bytes4 = ulid_bytes[4]
    ulid_bytes5 = ulid_bytes[5]
    ulid_bytes6 = ulid_bytes[6]
    ulid_bytes7 = ulid_bytes[7]
    ulid_bytes8 = ulid_bytes[8]
    ulid_bytes9 = ulid_bytes[9]
    ulid_bytes10 = ulid_bytes[10]
    ulid_bytes11 = ulid_bytes[11]
    ulid_bytes12 = ulid_bytes[12]
    ulid_bytes13 = ulid_bytes[13]
    ulid_bytes14 = ulid_bytes[14]
    ulid_bytes15 = ulid_bytes[15]
    enc = _ENCODE
    return (
        enc[(ulid_bytes0 & 224) >> 5]
        + enc[ulid_bytes0 & 31]
        + enc[(ulid_bytes1 & 248) >> 3]
        + enc[((ulid_bytes1 & 7) << 2) | ((ulid_bytes2 & 192) >> 6)]
        + enc[((ulid_bytes2 & 62) >> 1)]
        + enc[((ulid_bytes2 & 1) << 4) | ((ulid_bytes3 & 240) >> 4)]
        + enc[((ulid_bytes3 & 15) << 1) | ((ulid_bytes4 & 128) >> 7)]
        + enc[(ulid_bytes4 & 124) >> 2]
        + enc[((ulid_bytes4 & 3) << 3) | ((ulid_bytes5 & 224) >> 5)]
        + enc[ulid_bytes5 & 31]
        + enc[(ulid_bytes6 & 248) >> 3]
        + enc[((ulid_bytes6 & 7) << 2) | ((ulid_bytes7 & 192) >> 6)]
        + enc[(ulid_bytes7 & 62) >> 1]
        + enc[((ulid_bytes7 & 1) << 4) | ((ulid_bytes8 & 240) >> 4)]
        + enc[((ulid_bytes8 & 15) << 1) | ((ulid_bytes9 & 128) >> 7)]
        + enc[(ulid_bytes9 & 124) >> 2]
        + enc[((ulid_bytes9 & 3) << 3) | ((ulid_bytes10 & 224) >> 5)]
        + enc[ulid_bytes10 & 31]
        + enc[(ulid_bytes11 & 248) >> 3]
        + enc[((ulid_bytes11 & 7) << 2) | ((ulid_bytes12 & 192) >> 6)]
        + enc[(ulid_bytes12 & 62) >> 1]
        + enc[((ulid_bytes12 & 1) << 4) | ((ulid_bytes13 & 240) >> 4)]
        + enc[((ulid_bytes13 & 15) << 1) | ((ulid_bytes14 & 128) >> 7)]
        + enc[(ulid_bytes14 & 124) >> 2]
        + enc[((ulid_bytes14 & 3) << 3) | ((ulid_bytes15 & 224) >> 5)]
        + enc[ulid_bytes15 & 31]
    )
