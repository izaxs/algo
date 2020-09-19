#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    using std::string;

    bool valid(string &s, int lo, int hi, int remain) {
        if (lo >= hi) return true;
        if (s[lo] == s[hi]) return valid(s, lo + 1, hi - 1, remain);
        if (remain <= 0) return false;
        return valid(s, lo + 1, hi, remain - 1) || valid(s, lo, hi - 1, remain - 1);
    }

    bool validPalindrome(string &s) {
        return valid(s, 0, s.size() - 1, 1);
    }
}

int main() {
    using namespace leetcode;
    string input = "fefhghfaef";
    bool output = validPalindrome(input);
    print_inputoutput(input, to_string(output));
    string input2 = "fefhgqhfaef";
    bool output2 = validPalindrome(input2);
    print_inputoutput(input2, to_string(output2));
}