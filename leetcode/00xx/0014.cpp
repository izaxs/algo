#include "common.hpp"

namespace leetcode {
    // using std::vector;
    // using std::string;

    string longestCommonPrefix(vector<string>& strs) {
        string output("");
        if (strs.size() == 0) return output;
        for (int iCol = 0; iCol < strs[0].size(); ++iCol) {
            char cur;
            for (int iRow = 0; iRow < strs.size(); ++iRow) {
                if (iRow == 0) cur = strs[iRow][iCol];
                if (strs[iRow][iCol] != cur) return output;
                if (iRow == strs.size() - 1) output += cur;
            }
        }
        return output;
    }

    void test_longestCommonPrefix() {
        vector<string> input = {"flower","flow","flight"};
        string output = longestCommonPrefix(input);
        print_inputoutput(to_string(input), output);
    }
}