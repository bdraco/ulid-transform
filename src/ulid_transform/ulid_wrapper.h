#include <string>

#ifndef ULID_WRAPPER_H
#define ULID_WRAPPER_H

std::string _cpp_ulid();
std::vector<uint8_t> _cpp_ulid_bytes();
std::string _cpp_ulid_at_time(double timestamp);
std::vector<uint8_t> _cpp_ulid_at_time_bytes(double timestamp);
std::string _cpp_ulid_to_bytes(const char * ulid_string);
std::string _cpp_bytes_to_ulid(std::string bytes_string);

#endif
