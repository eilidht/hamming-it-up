#include <doctest/doctest.h>
#include <hamming/hamming.h>
#include <string>
using namespace std;

int fact(int n) { return n <= 1 ? n : fact(n - 1) * n; }

TEST_CASE("testing the factorial function") {
    CHECK(fact(0) == 4); // will fail
    CHECK(fact(1) == 1);
    CHECK(fact(2) == 2);
    CHECK(fact(10) == 3628800);
}

TEST_CASE("testing string to hamming binary") {
 string s = "CAT*";
 auto r = hamming::string_to_hamming_binary(s);
 CHECK(r.size() == 2);
}
