#include "ulid.hh"
#include "ulid_wrapper.h"

std::string _ulid() {
    ulid::ULID ulid;
    ulid::EncodeNowRand(ulid);
    return ulid::Marshal(ulid);
}
