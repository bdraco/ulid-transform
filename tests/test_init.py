import time

import pytest

from ulid_transform import (
    bytes_to_ulid,
    bytes_to_ulid_or_none,
    ulid_at_time,
    ulid_at_time_bytes,
    ulid_hex,
    ulid_now,
    ulid_now_bytes,
    ulid_to_bytes,
    ulid_to_bytes_or_none,
)


def test_ulid_now():
    ulid_str = ulid_now()
    assert len(ulid_str) == 26
    timestamp = _ulid_timestamp(ulid_str)
    assert timestamp == pytest.approx(int(time.time() * 1000), 1)


def test_ulid_now_bytes():
    ulid_bytes = ulid_now_bytes()
    assert len(ulid_bytes) == 16
    timestamp = _ulid_timestamp(ulid_bytes)
    assert timestamp == pytest.approx(int(time.time() * 1000), 1)


def test_ulid_hex():
    ulid_str = ulid_hex()
    assert len(ulid_str) == 32


def test_ulid_to_bytes():
    assert (
        ulid_to_bytes("01GTCKZT7K26YEVVW6AMQ3J0VT")
        == b"\x01\x86\x99?\xe8\xf3\x11\xbc\xed\xef\x86U.9\x03z"
    )


def test_ulid_to_bytes_overflow():
    with pytest.raises(ValueError):
        ulid_to_bytes("01GTCKZT7K26YEVVW6AMQ3J0VT0000")


def test_ulid_to_bytes_under_low():
    with pytest.raises(ValueError):
        ulid_to_bytes("01")


def test_bytes_to_ulid():
    assert (
        bytes_to_ulid(b"\x01\x86\x99?\xe8\xf3\x11\xbc\xed\xef\x86U.9\x03z")
        == "01GTCKZT7K26YEVVW6AMQ3J0VT"
    )


def test_ulid_to_bytes_invalid_length():
    with pytest.raises(ValueError):
        assert ulid_to_bytes("aa")


def test_bytes_to_ulid_invalid_length():
    with pytest.raises(ValueError, match="aa"):
        assert bytes_to_ulid(b"aa")


def test_ulid_to_bytes_2():
    assert (
        ulid_to_bytes("00000000AC00GW0X476W5TVBFE")
        == b"\x00\x00\x00\x00\x01L\x00!\xc0t\x877\x0b\xad\xad\xee"
    )


def test_timestamp_string():
    ulid = ulid_at_time(1677627631.2127638)
    assert ulid[:10] == "01GTD6C9KC"


def test_timestamp_bytes():
    ulid = ulid_at_time_bytes(1677627631.2127638)
    # prefix verified with another ulid implementation (valohai/ulid2)
    assert ulid[:6] == b"\x01\x86\x9af&l"


@pytest.mark.parametrize("gen", [ulid_at_time, ulid_at_time_bytes])
def test_timestamp(gen):
    now = time.time()
    ulid = gen(now)
    # ULIDs store time to 3 decimal places compared to python timestamps
    assert _ulid_timestamp(ulid) == int(now * 1000)


@pytest.mark.parametrize("gen", [ulid_at_time, ulid_at_time_bytes])
def test_timestamp_fixed(gen):
    now = 1677627631.2127638
    ulid = gen(now)
    # ULIDs store time to 3 decimal places compared to python timestamps
    assert _ulid_timestamp(ulid) == int(now * 1000)


def _ulid_timestamp(ulid: str | bytes) -> int:
    if not isinstance(ulid, bytes):
        from ulid_transform import ulid_to_bytes

        ulid_bytes = ulid_to_bytes(ulid)
    else:
        ulid_bytes = ulid
    return int.from_bytes(b"\x00\x00" + ulid_bytes[:6], "big")


def test_non_uppercase_b32_data():
    assert len(ulid_to_bytes("not_uppercase_b32_data_:::")) == 16


def test_ulid_to_bytes_or_none() -> None:
    """Test ulid_to_bytes_or_none."""

    assert (
        ulid_to_bytes_or_none("01EYQZJXZ5Z1Z1Z1Z1Z1Z1Z1Z1")
        == b"\x01w\xaf\xf9w\xe5\xf8~\x1f\x87\xe1\xf8~\x1f\x87\xe1"
    )
    assert ulid_to_bytes_or_none("invalid") is None
    assert ulid_to_bytes_or_none(None) is None


def test_bytes_to_ulid_or_none() -> None:
    """Test bytes_to_ulid_or_none."""

    assert (
        bytes_to_ulid_or_none(b"\x01w\xaf\xf9w\xe5\xf8~\x1f\x87\xe1\xf8~\x1f\x87\xe1")
        == "01EYQZJXZ5Z1Z1Z1Z1Z1Z1Z1Z1"
    )
    assert bytes_to_ulid_or_none(b"invalid") is None
    assert bytes_to_ulid_or_none(None) is None
