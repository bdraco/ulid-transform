from cpython cimport array

import array


cdef array.array decoding = array.array(
    'B',
    (0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x01,
     0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E,
     0x0F, 0x10, 0x11, 0x01, 0x12, 0x13, 0x01, 0x14, 0x15, 0x00,
     0x16, 0x17, 0x18, 0x19, 0x1A, 0xFF, 0x1B, 0x1C, 0x1D, 0x1E,
     0x1F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0A, 0x0B, 0x0C,
     0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x01, 0x12, 0x13, 0x01, 0x14,
     0x15, 0x00, 0x16, 0x17, 0x18, 0x19, 0x1A, 0xFF, 0x1B, 0x1C,
     0x1D, 0x1E, 0x1F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
     0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF)
)

cpdef decode_ulid(str encoded)

cdef inline _decode_ulid(const char *encoded):
    return bytes((
        ((decoding[encoded[0]] << 5) | decoding[encoded[1]]) & 0xFF,
        ((decoding[encoded[2]] << 3) | (decoding[encoded[3]] >> 2)) & 0xFF,
        ((decoding[encoded[3]] << 6) | (decoding[encoded[4]] << 1) | (decoding[encoded[5]] >> 4)) & 0xFF,
        ((decoding[encoded[5]] << 4) | (decoding[encoded[6]] >> 1)) & 0xFF,
        ((decoding[encoded[6]] << 7) | (decoding[encoded[7]] << 2) | (decoding[encoded[8]] >> 3)) & 0xFF,
        ((decoding[encoded[8]] << 5) | (decoding[encoded[9]])) & 0xFF,
        ((decoding[encoded[10]] << 3) | (decoding[encoded[11]] >> 2)) & 0xFF,
        ((decoding[encoded[11]] << 6) | (decoding[encoded[12]] << 1) | (decoding[encoded[13]] >> 4)) & 0xFF,
        ((decoding[encoded[13]] << 4) | (decoding[encoded[14]] >> 1)) & 0xFF,
        ((decoding[encoded[14]] << 7) | (decoding[encoded[15]] << 2) | (decoding[encoded[16]] >> 3)) & 0xFF,
        ((decoding[encoded[16]] << 5) | (decoding[encoded[17]])) & 0xFF,
        ((decoding[encoded[18]] << 3) | (decoding[encoded[19]] >> 2)) & 0xFF,
        ((decoding[encoded[19]] << 6) | (decoding[encoded[20]] << 1) | (decoding[encoded[21]] >> 4)) & 0xFF,
        ((decoding[encoded[21]] << 4) | (decoding[encoded[22]] >> 1)) & 0xFF,
        ((decoding[encoded[22]] << 7) | (decoding[encoded[23]] << 2) | (decoding[encoded[24]] >> 3)) & 0xFF,
        ((decoding[encoded[24]] << 5) | (decoding[encoded[25]])) & 0xFF
    ))
