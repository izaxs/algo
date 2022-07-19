#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    using std::string;

    bool isPalindromeHelper(string &s, int lo, int hi) {
        while (lo < hi) {
            if (!std::isalnum(s[lo])) lo++;
            else if (!std::isalnum(s[hi])) hi--;
            else if (tolower(s[lo++]) != tolower(s[hi--])) return false;
        }
        return true;
    }

    bool isPalindrome(string s) {
        return isPalindromeHelper(s, 0, s.size() - 1);
    }

    bool isPalindrome2(string s) {
        int lo = 0, hi = s.size() - 1;
        while (lo < hi) {
            if (!std::isalnum(s[lo])) lo++;
            else if (!std::isalnum(s[hi])) hi--;
            else if (tolower(s[lo++]) != tolower(s[hi--])) return false;
        }
        return true;
    }
}

int main() {
    using namespace leetcode;
    string input = "A man, a plan, a canal: Panama";
    bool output = isPalindrome2(input);
    print_inputoutput(input, to_string(output));
}