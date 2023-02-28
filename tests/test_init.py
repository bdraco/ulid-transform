import pytest

from ulid_transform import ulid_hex, ulid_now, ulid_to_bytes


def test_ulid_now():
    ulid_str = ulid_now()
    assert len(ulid_str) == 26


def test_ulid_hex():
    ulid_str = ulid_hex()
    assert len(ulid_str) == 32


def test_ulid_to_bytes():
    assert (
        ulid_to_bytes("01GTCKZT7K26YEVVW6AMQ3J0VT")
        == b"\x01\x86\x99?\xe8\xf3\x11\xbc\xed\xef\x86U.9\x03z"
    )


def test_ulid_to_bytes_invalid_length():
    with pytest.raises(ValueError):
        assert ulid_to_bytes("aa")


def test_ulid_to_bytes_2():
    assert (
        ulid_to_bytes("00000000AC00GW0X476W5TVBFE")
        == b"\x00\x00\x00\x00\x01L\x00!\xc0t\x877\x0b\xad\xad\xee"
    )
