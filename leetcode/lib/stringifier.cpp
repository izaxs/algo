#include <string>
#include <vector>

#include "../include/typeutil.hpp"

namespace leetcode {
    using std::string;

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