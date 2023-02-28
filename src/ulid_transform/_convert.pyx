#ifdef ULIDUINT128
#include "ulid_uint128.hh"
#else
#include "ulid_struct.hh"
#endif // ULIDUINT128

from libcpp.vector cimport vector


def ulid_to_bytes(char *encoded)
    ulid::ULID ulid;
    std::vector<uint8_t> m = ulid::MarshalBinary(encoded);
