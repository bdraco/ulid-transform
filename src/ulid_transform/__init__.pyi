def ulid_hex() -> str: ...
def ulid_at_time_bytes(timestamp: float) -> bytes: ...
def ulid_now_bytes() -> bytes: ...
def ulid_now() -> str: ...
def ulid_at_time(timestamp: float) -> str: ...
def ulid_to_bytes(value: str) -> bytes: ...
def bytes_to_ulid(value: bytes) -> str: ...
def ulid_to_bytes_or_none(ulid: str | None) -> bytes | None: ...
def bytes_to_ulid_or_none(ulid_bytes: bytes | None) -> str | None: ...
def ulid_to_timestamp(ulid: str | bytes) -> int: ...