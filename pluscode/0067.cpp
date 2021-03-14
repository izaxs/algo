#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    using std::string;
    using std::reverse;

    string addBinary(string a, string b) {
        int val = 0, ia = a.size() - 1, ib = b.size() - 1;
        string output;
        while (ia >= 0 || ib >= 0 || val > 0) {
            if (ia >= 0) val += a[ia--] - '0';
            if (ib >= 0) val += b[ib--] - '0';
            output += '0' + (val & 1);
            val >>= 1;
        }
        reverse(output.begin(), output.end());
        return output.size() > 0 ? output : "";
    }
}

int main() {
    using namespace leetcode;
    string input1 = "011001";
    string input2 = "11001";
    string output = addBinary(input1, input2);
    print_inputoutput(input1 + " & " + input2, output);
}