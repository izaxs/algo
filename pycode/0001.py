class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        want = {}
        for i, v in enumerate(nums):
            if v not in want:
                want[target-v] = i
            else:
                return [want[v], i]
        return []

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        want: dict[int, int] = {}
        for i, v in enumerate(nums):
            if (lastI := want.get(v)) is not None:
                return [lastI, i]
            want[target-v] = i
        return []

if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 5, 9, -4, 0, 7]
    target = 1
    print(s.twoSum(nums, target))