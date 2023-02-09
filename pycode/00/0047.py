# Permutations II


# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Constraints:

#     1 <= nums.length <= 8
#     -10 <= nums[i] <= 10

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res: list[list[int]] = []
        used = [False]*len(nums)
        def search(temp: list[int]):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            for i, v in enumerate(nums):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]): continue
                used[i] = True
                temp.append(v)
                search(temp)
                temp.pop()
                used[i] = False
        search([])
        return res