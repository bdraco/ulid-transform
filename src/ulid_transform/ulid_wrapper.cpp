
#ifdef ULIDUINT128
#include "ulid_uint128.hh"
#else
#include "ulid_struct.hh"
#endif // ULIDUINT128

#include "ulid_wrapper.h"

std::string _ulid() {
    ulid::ULID ulid;
    ulid::EncodeNowRand(ulid);
    return ulid::Marshal(ulid);
}
