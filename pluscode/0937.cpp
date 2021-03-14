#include "../include/common.hpp"
#include <cctype>

namespace leetcode {
    using namespace utilities;
    using std::vector;
    using std::string;

    vector<string> reorderLogFiles(vector<string>& logs) {
        std::stable_sort(logs.begin(), logs.end(), [](auto &a, auto &b) {
            auto aLo = a.find_first_of(' ') + 1;
            auto bLo = b.find_first_of(' ') + 1;
            auto aIsDigit = std::isdigit(a[aLo]);
            auto bIsDigit = std::isdigit(b[bLo]);
            bool result;
            if (!aIsDigit && !bIsDigit) {
                auto contentCmp = a.compare(aLo, a.size(), b, bLo, b.size());
                if (contentCmp) {
                    result = contentCmp < 0 ? true : false;
                } else {
                    result = a.compare(0, aLo, b, 0, bLo) < 0 ? true : false;
                }
            } else if (aIsDigit ^ bIsDigit) {
                result = !aIsDigit ? true : false;
            }
            return result;
        });
        return logs;
    }

    // Better solution!
    vector<string> reorderLogFiles2(vector<string>& logs) {
        auto iter = std::stable_partition(logs.begin(), logs.end(),[](const string& s) {
            return std::isalpha(s[s.find_first_of(' ') + 1]);
        });
        std::stable_sort(logs.begin(), iter, [](const string &a, const string &b) {
            auto aLo = a.find_first_of(' ') + 1;
            auto bLo = b.find_first_of(' ') + 1;
            auto cmpResult = a.compare(aLo, a.size(), b, bLo, b.size());
            if (cmpResult) return cmpResult < 0 ? true : false;
            return a.compare(0, aLo, b, 0, bLo) ? true : false;
        });
        return logs;
    }
}

int main() {
    using namespace leetcode;
    vector<string> input = {"dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"};
    auto inputStr = to_string(input);
    auto output = reorderLogFiles2(input);
    print_inputoutput(inputStr, to_string(output));
}