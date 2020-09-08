#pragma once
#include <string>
#include <vector>

namespace leetcode {
    template<typename T>
    std::string stringify(std::vector<T> nums) {
        using namespace std;
        string output = "{ ";
        for (int i = 0; i < nums.size(); i++) {
            output += to_string(nums[i]);
            if (i != nums.size() - 1) {
                output += ", ";
            }
        }
        output += " }";
        return output;
    }
}