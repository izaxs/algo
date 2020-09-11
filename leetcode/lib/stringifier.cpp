#include <string>
#include <vector>

#include "../include/typeutil.hpp"

namespace leetcode {
    using std::string;

    string to_string(const string &s) {
        return s;
    }

    string to_string(const char* t) {
        return t;
    }

    string to_string(ListNode *head) {
        string output = "{ ";
        while (head != nullptr) {
            output += std::to_string(head->val);
            if (head->next != nullptr) {
                output += " -> ";
            }
            head = head->next;
        }
        output += " }";
        return output;
    }
}