#include "common.hpp"

namespace leetcode {
    using namespace utilities;

    void reverseString(vector<char>& s) {
        int end = s.size() - 1;
        int half = s.size() / 2;
        for (int i = 0; i < half; ++i) {
            s[i] ^= s[end - i];
            s[end - i] ^= s[i];
            s[i] ^= s[end - i];
        }
    }

    // C++ way
    void reverseString2(vector<char>& s) {
        int i = 0, j = s.size() - 1;
        while (i < j) std::swap(s[i++], s[j--]);
    }

    // Not in place, but elegant
    void reverseString3(vector<char>& s) {
        s = {s.rbegin(), s.rend()};
    }

    // Also good
    void reverseString4(vector<char>& s) {
        std::reverse(s.begin(), s.end());
    }
}

int main() {
    using namespace leetcode;
    vector<char> s1 = {'a', 'b', 'c', 'd', 'e', 'f'}, s2 = s1;
    reverseString4(s2);
    print_inputoutput(to_string(s1), to_string(s2));
}