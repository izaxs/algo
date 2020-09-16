#include "common.hpp"

namespace leetcode {
    using std::vector;
    using std::stack;
    using std::string;

    bool hasValidParentheses(string s) {
        vector<char> left{'(', '{', '['};
        vector<char> right{')', '}', ']'};
        stack<char> stk;
        for (char &ch : s) {
            if (auto it = std::find(right.begin(), right.end(), ch); it != right.end()) {
                if (stk.empty()) return false;
                char expect = left[std::distance(right.begin(), it)];
                if (expect != stk.top()) return false;
                stk.pop();
            } else {
                stk.push(ch);
            }
        }
        return stk.empty() ? true : false;
    }

    bool hasValidParentheses2(string s) {
        stack<char> stk;
        for (char &ch : s) {
            switch (ch) {
                case '(': stk.push(')'); break;
                case '{': stk.push('}'); break;
                case '[': stk.push(']'); break;
                default:
                    if (stk.empty() || stk.top() != ch) return false;
                    stk.pop();
            }
        }
        return stk.empty() ? true : false;
    }
}

int main() {
    using namespace leetcode;
    // string input = "{}({[]})";
    string input = "([]{[])";
    auto output = hasValidParentheses2(input);
    print_inputoutput(input, to_string(output));
}