# Permutations

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Constraints:

#     1 <= nums.length <= 6
#     -10 <= nums[i] <= 10
#     All the integers of nums are unique.

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        used = [False]*len(nums)
        temp: list[int] = []
        res: list[list[int]] = []
        def search():
            if len(temp) == len(nums): 
                res.append(temp[:])
                return
            for i, v in enumerate(nums):
                if used[i]: continue
                used[i] = True
                temp.append(v)
                search()
                temp.pop()
                used[i] = False
        search()
        return res

    def permute2(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        temp: list[int] = []
        def search(remain: list[int]):
            if not remain: 
                res.append(temp[:])
                return
            for i, n in enumerate(remain):
                temp.append(n)
                search(remain[:i]+remain[i+1:])
                temp.pop()
        search(nums)
        return res

        
if __name__ == "__main__":
    Solution().permute([1,2,3])