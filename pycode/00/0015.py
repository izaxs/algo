# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Constraints:

#     3 <= nums.length <= 3000
#     -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3: return []
        nums.sort()
        results: set[tuple[int, int, int]] = set()
        for x in range(len(nums)-2):
            lo, hi = x + 1, len(nums)-1
            while lo < hi:
                curSum = nums[x] + nums[lo] + nums[hi]
                if curSum == 0:
                    results.add((nums[x], nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
                elif curSum < 0:
                    lo += 1
                else:
                    hi -= 1
        return [[x, y, z] for x, y, z in results]
    
    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        for x in range(len(nums) - 2):
            if x > 0 and nums[x] == nums[x - 1]: continue
            y, z = x + 1, len(nums)-1
            while y < z:
                curSum = nums[x] + nums[y] + nums[z]
                if curSum < 0:
                    y += 1
                elif curSum > 0:
                    z -= 1
                else:
                    results.append([nums[x], nums[y], nums[z]])
                    while y < z and nums[y] == nums[y + 1]: y += 1
                    while y < z and nums[z] == nums[z - 1]: z -= 1
                    y += 1
                    z -= 1
        return results
    
if __name__ == "__main__":
    res = Solution().threeSum([3,0,-2,-1,1,2])
    print(res)