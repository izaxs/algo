# [0, 1, 2, 3] => [0, 1, 2, 3]
# [3, 1, 2, 0] => [-1, -1, -1, 3]
# [2, 0, 1, 3] => [-1, 0, 2, 3]

class Solution:
    def process(self, nums: list[int]) -> list[int]:
        L, cur = len(nums), 0
        isProcessed = [False] * L
        result = [-1] * L
        for i, n in enumerate(nums):
            isProcessed[n] = True
            while cur < L and isProcessed[cur]: cur += 1
            if cur >= n + 1: result[i] = cur-1
        return result
    
if __name__ == '__main__':
    inputs = [0, 1, 2, 3]
    inputs = [3, 1, 2, 0]
    inputs = [2, 0, 1, 3]
    result = Solution().process(inputs)
    print(result)
            