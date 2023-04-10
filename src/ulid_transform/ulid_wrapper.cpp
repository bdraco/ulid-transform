#include "ulid_wrapper.h"
#include "ulid.hh"

using namespace std;

std::string _cpp_ulid() {
  ulid::ULID ulid;
  ulid::EncodeTimeSystemClockNow(ulid);
  ulid::EncodeEntropyRand(ulid);
  return ulid::Marshal(ulid);
}

std::string _cpp_ulid_at_time(double epoch_time) {
  ulid::ULID ulid;
  std::time_t t = epoch_time;
  int microseconds = (epoch_time - t) * 1000000;
  std::chrono::system_clock::time_point time = std::chrono::system_clock::from_time_t(t) + std::chrono::microseconds(microseconds);
  ulid::EncodeTime(time, ulid);
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
