#include "ulid_wrapper.h"
#include "ulid.hh"
#include<iostream>
using namespace std;

std::string _cpp_ulid() {
  ulid::ULID ulid;
  ulid::EncodeNowRand(ulid);
  std::string mystr = ulid::Marshal(ulid);
  std::cerr << mystr;
  return mystr;
}

std::string _cpp_ulid_at_time(double epoch_time) {
  time_t encoded_time = static_cast<time_t>(epoch_time*1000);
  ulid::ULID ulid;
  ulid::EncodeTime(encoded_time, ulid);
  ulid::EncodeEntropyRand(ulid);
  return ulid::Marshal(ulid);
}

std::string _cpp_ulid_to_bytes(std::string ulid_string) {
  ulid::ULID ulid;
  ulid::UnmarshalFrom(ulid_string.c_str(), ulid);
  std::vector<uint8_t> data = ulid::MarshalBinary(ulid);
  std::string str(reinterpret_cast<char *>(data.data()), data.size());
  return str;
}
