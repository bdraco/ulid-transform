__version__ = "0.2.0"

# Fast ulid is used for generation
from fast_ulid import ulid

from .convert import ulid_to_bytes

__all__ = ["ulid", "ulid_to_bytes"]
