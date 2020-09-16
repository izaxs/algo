#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    using std::max;
    using std::vector;
    using std::unordered_map;

    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> indexes;
        int maxLen = 0, lo = 0;
        for (int hi = 0; hi < s.size(); hi++) {
            auto iter = indexes.find(s[hi]);
            if (iter == indexes.end()) {
                indexes[s[hi]] = hi;
                maxLen =  max(hi - lo + 1, maxLen);
                continue;
            }
            for (int rm = lo; rm < iter->second; rm++) {
                indexes.erase(s[rm]);
            }
            lo = iter->second + 1;
            indexes[s[hi]] = hi;
        }
        return maxLen;
    }

    // The better one learned
    int lengthOfLongestSubstring2(string s) {
        vector<int> table(256, -1);
        int maxLen = 0, lo = -1;
        for (int hi = 0; hi < s.size(); hi++) {
            if (table[s[hi]] > lo) lo = table[s[hi]];
            table[s[hi]] = hi;
            maxLen = max(maxLen, hi - lo);
        }
        return maxLen;
    }
}

int main() {
    using namespace leetcode;
    string input = "abcbhnmkmuy";
    int result = lengthOfLongestSubstring2(input);
    std::cout << "input: " << input << std::endl;
    std::cout << "expect: 6, actual: " << result << std::endl;

    string input2 = "abbkjbbbjbbghayyi";
    int result2 = lengthOfLongestSubstring2(input2);
    std::cout << "input2: " << input2 << std::endl;
    std::cout << "expect: 5, actual: " << result2 << std::endl;
}