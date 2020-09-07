#include <iostream>

#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <unordered_map>
#include <map>

// #include "catch.hpp"
#include "cassert"

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

