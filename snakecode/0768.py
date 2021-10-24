class Solution:
    # arr is random
    def maxChunksToSorted(self, arr: list[int]) -> int:
        m = len(arr)
        suffixMin = arr[:]
        for i in range(m-2, -1, -1):
            suffixMin[i] = min(arr[i], suffixMin[i+1])
        curMax = arr[0]
        result = 1
        for i in range(1, m):
            if curMax <= suffixMin[i]: result += 1
            curMax = max(curMax, arr[i])
        return result
