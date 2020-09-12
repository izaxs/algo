#include "../include/common.hpp"
#include <limits>

namespace leetcode {
    using std::string;
    
    int myAtoi(string str) {
        if (str.empty()) return 0;
        int i = -1, num = 0, sign = 1, maxInt = std::numeric_limits<int>::max();
        int threshold = maxInt / 10, thresholdDigit = maxInt % 10;
        while (str[++i] == ' ');
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

    void test_myAtoi() {
        string input = "  -1319238 kgj";
        auto output = to_string(myAtoi(input));
        print_inputoutput(input, output);
    }
}