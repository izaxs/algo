#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    using std::string;
    using std::to_string;

    string countAndSay(int n) {
        if (n == 1) return "1";
        string last = countAndSay(n - 1);
        string res;
        int i = 0, count = 1;
        while (++i < last.length()) {
            if (last[i] == last[i - 1]) {
                ++count;
            } else {
                res += to_string(count) + last[i - 1];
                count = 1;
            }
        };
        if (count > 0) {
            res += to_string(count) + last[i - 1];
        }
        return res;
    }
}

int main() {
    using namespace leetcode;
    int input = 5;
    auto output = countAndSay(input);
    print_inputoutput(to_string(input), output);
}