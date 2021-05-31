#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    using std::string;

    int firstUniqChar(string &s) {
        int freq[26] = {};
        for (auto &ch : s) ++freq[ch - 'a'];
        for (int i = 0; i < s.size(); i++) {
            if (freq[s[i] - 'a'] == 1) return i;
        }
        return -1;
    }
}

int main() {
    using namespace leetcode;
    string input = "loveleetcode";
    int output = firstUniqChar(input);
    print_inputoutput(input, to_string(output));
}