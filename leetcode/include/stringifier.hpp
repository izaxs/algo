#pragma once
#include <string>
#include <vector>

namespace leetcode {
    using std::string;
    using std::vector;

    template<typename T>
    string to_string(vector<T> nums) {
        string output = "{ ";
        for (int i = 0; i < nums.size(); i++) {
            output += std::to_string(nums[i]);
            if (i != nums.size() - 1) {
                output += ", ";
            }
        }
        output += " }";
        return output;
    }

    string to_string(ListNode *head);
}