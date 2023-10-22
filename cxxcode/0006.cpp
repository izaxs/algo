#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    using std::string;
    using std::vector;

    string convertZigZag(string s, int numRows) {
        if (numRows <= 1) return s;
        vector<string> zigzag(numRows, "");
        for (int i = 0, r = 0, nextR = 0; i < s.size(); i++) {
            zigzag[r] += s[i];
            if (r == numRows - 1) nextR = -1;
            if (r == 0) nextR = 1;
            r += nextR;
        }
        string output;
        for (auto s: zigzag) output += s;
        return output;
    }
}

int main() {
    using namespace leetcode;
    string input = "PAYPALISHIRING";
    auto output = convertZigZag(input, 3);
    print_inputoutput(input, output);
}