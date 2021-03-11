#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    using std::cout;
    using std::endl;
    using std::vector;
    using hmap = std::unordered_map<int, int>;

    vector<int> twoSum(vector<int>& nums, int target) {
        hmap visited;
        for (int i = 0; i < nums.size(); i++) {
            auto j = visited.find(target - nums[i]);
            if (j != visited.end()) {
                return {j->second, i};
            }
            visited[nums[i]] = i;
        }
        return {};
    }
}

int main() {
    using namespace leetcode;
    vector<int> input{5, 0, 9, 10, 1, -7};
    int target = 3;
    auto output = twoSum(input, target);
    print_inputoutput(to_string(input), to_string(output));
}