#include "common.hpp"

namespace leetcode {
    using std::string;

    void expand(string &s, int lo, int hi, int &maxLo, int &maxLen) {
        while (lo >= 0 && hi < s.size()) {
            if (s[lo] != s[hi]) return;
            int curLen = hi - lo + 1;
            if (curLen > maxLen) {
                maxLo = lo;
                maxLen = curLen;
            }
            lo--, hi++;
        }
    }

    string longestPalindrome(string s) {
        int maxLo = 0, maxLen = 0, size = s.size();
        for (int i = 0; i < size; i++) {
            if (size - i <= maxLen / 2) break;
            expand(s, i, i, maxLo, maxLen);
            expand(s, i, i + 1, maxLo, maxLen);
        }
        return s.substr(maxLo, maxLen);
    }

    // Bad solution, time exceeded
    bool isPalindrome0(string s, int lo, int hi) {
        while (lo < hi) {
            if (s[lo++] != s[hi--]) return false;
        }
        return true;
    }

    string longestPalindrome0(string s) {
        int len = s.size();
        while (len > 0) {
            for (int i = 0; i + len <= s.size(); i++) {
                if (isPalindrome0(s, i, i + len - 1)) return s.substr(i, len);
            }
            len--;
        }
        return "";
    }
}

int main() {
    using namespace leetcode;
    string input = "babad";
    string output = longestPalindrome(input);
    print_inputoutput(input, output);

    // string input = "aabcbefebcde";
    // string output = longestPalindrome(input);
    // print_inputoutput(input, output);
}