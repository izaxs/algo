#include "common.hpp"
#include <limits>

namespace leetcode {
    using namespace utilities;
    using std::string;
    
    int myAtoi(string str) {
        int i = -1, num = 0, sign = 1;
        int maxInt = std::numeric_limits<int>::max();
        int threshold = maxInt / 10, thresholdDigit = maxInt % 10;
        while (str[++i] == ' ' && i < str.size());
        if (str[i] == '+' || str[i] == '-') {
            sign = str[i++] == '+' ? 1 : -1;
        }
        for (;str[i] >= '0' && str[i] <= '9'; i++) {
            int digit = str[i] - '0';
            if (num > threshold || (num == threshold && digit > thresholdDigit)) {
                return sign == 1 ? maxInt : -maxInt - 1;
            }
            num = 10 * num + digit;
        }
        return num * sign;
    }
}

int main() {
    using namespace leetcode;
    // string input = "  -1319238 kgj";
    string input = "   -kk";
    auto output = to_string(myAtoi(input));
    print_inputoutput(input, output);
}