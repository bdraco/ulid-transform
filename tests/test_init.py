import pytest

from ulid_transform import ulid, ulid_hex, ulid_to_bytes


def test_ulid():
    ulid_str = ulid()
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
