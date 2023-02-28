import pytest

from ulid_transform import decode_ulid, ulid


def test_ulid():
    ulid_str = ulid()
    assert len(ulid_str) == 26


def test_decode_ulid():
    assert (
        decode_ulid("01GTCKZT7K26YEVVW6AMQ3J0VT")
        == b"\x01\x86\x99?\xe8\xf3\x11\xbc\xed\xef\x86U.9\x03z"
    )


def test_decode_ulid_invalid_length():
    with pytest.raises(ValueError):
        assert decode_ulid("aa")
