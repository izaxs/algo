class Solution:
    # arr is 0 -> N-1
    def maxChunksToSorted(self, arr: list[int]) -> int:
        i, upper, result = 0, arr[0], 1
        while i < len(arr):
            upper = max(upper, arr[i])
            if i == upper:
                result += 1
            i += 1
        return result
