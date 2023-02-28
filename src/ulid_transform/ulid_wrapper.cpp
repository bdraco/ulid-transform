#include "ulid.hh"
#include "ulid_wrapper.h"
#include <chrono>

using namespace std;


std::string _cpp_ulid() {
    ulid::ULID ulid;
    ulid::EncodeNowRand(ulid);
    return ulid::Marshal(ulid);
}

std::string _cpp_ulid_at_time(double timestamp) {
    const auto encoded_time = chrono::system_clock::to_time_t(chrono::system_clock::time_point(chrono::duration_cast<chrono::seconds>(chrono::duration<double>(timestamp))));
    ulid::ULID ulid;
    ulid::EncodeTime(encoded_time, ulid);
    ulid::EncodeEntropyRand(ulid);
    return ulid::Marshal(ulid);
}

std::string _cpp_ulid_to_bytes(std::string ulid_string) {
    ulid::ULID ulid = ulid::Unmarshal(ulid_string.c_str());
    std::vector<uint8_t> data = ulid::MarshalBinary(ulid);
    std::string str(reinterpret_cast<char*>(data.data()), data.size());
    return str;
}
