#include "common.hpp"

namespace leetcode {
    using namespace utilities;

    string reverseStringV2(string s, int k) {
        bool rev = true, stop = false;
        int lo = 0, hi = 0;
        do {
            if (lo + k >= s.size()) {
                stop = true;
                hi = s.size() - 1;
            } else {
                hi = lo + k - 1;
            }
            if (rev) {
                for (int i = lo, j = hi; i < j;) {
                    std::swap(s[i++], s[j--]);
                }
            }
            rev = !rev;
            lo += k;
        } while (!stop);
        return s;
    }

    // Better solution
    string reverseStringV22(string s, int k) {
        for (int i = 0; i < s.size(); i += k * 2) {
            auto hi = std::min(s.begin() + i + k, s.end());
            std::reverse(s.begin() + i, hi);
        }
        return s;
    }
}

int main() {
    using namespace leetcode;
    string input1 = "abcdefghijklmn";
    int input2 = 3;
    string output = reverseStringV22(input1, input2);
    print_inputoutput(input1 + ", " + to_string(input2), output);
}