
#include <array>
#include <hamming/hamming.h>
namespace hamming{
using std::string;
using std::vector;
using std::uint8_t;
using std::uint64_t;
using std::array;

template<int n_elements, typename int_type>
using bit_vect = array<int_type, n_elements>;// a fixed size array/memoryblock

using my_vect = bit_vect<8, int8_t>;

inline my_vect f_xor(my_vect const& a, my_vect const& b) {
    my_vect r;
    for (size_t i = 0;i < a.size();++i)
        r[i] = a[i] ^ b[i];
    return r;
}

inline uint64_t count_bits(my_vect const& a) {
    uint64_t sum{ 0 };
    for (auto v : a) {// v uint8_t, 1000 0010 
        for (auto i = 0u;i < sizeof(my_vect::value_type);++i) {
            sum += (v & 1);
            v = v >> 1;// move all bits one to the right
        }
    }
    return sum;
}

auto use_my_f_xor() {
    my_vect a{ 0,5,7,9,0,0,0,0 };
    my_vect b{ 1,2,3,4,5,6,7,8 };
    auto r = f_xor(a, b);
    return count_bits(r);
}


inline int bin_or(int a, int b) {
    return a ^ b;
}

inline uint8_t char_to_hamming_binary(char x) {
    switch (x) {
    case'A':return 1;
    case'C':return 2;
    case'G':return 4;
    case'T':return 8;
    }
    return 0;
}


vector<uint8_t> string_to_hamming_binary(string const& s) {
    vector<uint8_t> r;
    r.reserve(1 + s.size() / 2);// allocating the size needed
    uint8_t e = 0;
    for (auto i = 0u;i < s.size();++i) {
        e = (e << 4) | char_to_hamming_binary(s[i]);
        if (i & 1) // every odd num, (pair of chars)
            r.emplace_back(e);//stash two letters to binary
    }
    return r;
}
#include <iostream>

// Hamming distance for 64-bit integers from wikipedia https://en.wikipedia.org/wiki/Hamming_distance
int hamming_distance64(unsigned long long x, unsigned long long y)
{
    return __builtin_popcountll(x ^ y);
}
}
//#include <iostream>
//int main() {
//    string s1 = "CAT";
//   string s2 = "TAT";
//    vector<uint8_t> b1 = string_to_hamming_binary(s1);
////    vector<uint8_t> b2 = string_to_hamming_binary(s2);
//    // auto r= f_xor(b1,b2);
//
//    //  int result = use_my_f_xor();
//    unsigned long long x = 1;
//    unsigned long long y = 7;
//    int result = hamming_distance64(x,y);
//
//    std::cout << result;
//}
