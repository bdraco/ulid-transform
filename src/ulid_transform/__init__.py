__version__ = "0.1.0"

# Fast ulid is used for generation
from fast_ulid import ulid

from .convert import decode_ulid

__all__ = ["ulid", "decode_ulid"]
