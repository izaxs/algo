def twoSum(nums: list[int], target: int) -> list[int]:
    want = {}
    for i, v in enumerate(nums):
        if v not in want:
            want[target - v] = i
        else:
            return [want[v], i]
    return []

nums = [3, 2, 5, 9, -4, 0, 7]
target = 1
print(twoSum(nums, target))