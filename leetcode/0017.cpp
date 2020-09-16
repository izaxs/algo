#include "common.hpp"

namespace leetcode {
    using std::vector;
    using std::string;

    vector<string> letterCombinations(string digits) {
        vector<char> bases = {'a', 'd', 'g', 'j', 'm', 'p', 't', 'w'};
        vector<string> output;
        if (digits.empty()) return output;
        output.push_back("");
        for (char &ch : digits) {
            int range = (ch == '9' || ch == '7') ? 4 : 3;
            char base = bases[ch - '2'];
            vector<string> additional;
            for (int i = 0; i < range; ++i) {
                for (auto &str : output) {
                    string cur(str);
                    cur += base + i;
                    additional.push_back(cur);
                }
            }
            output.swap(additional);
        }
        return output;
    }
}

int main() {
    using namespace leetcode;
    string input = "45";
    auto output = letterCombinations(input);
    print_inputoutput(input, to_string(output));
}