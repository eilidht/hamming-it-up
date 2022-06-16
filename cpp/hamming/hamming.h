#pragma once
#include <cstdint>
#include <vector>
#include <string>
namespace hamming{
    using std::string;
    using std::vector;
    using std::uint8_t;
    vector<uint8_t> string_to_hamming_binary(string const& s);
}
