class Solution:
    def trap(self, height: list[int]) -> int:
        globalHigh = -1 << 32
        lo, hi = 0, len(height)-1
        trapped = 0
        while lo < hi:
            curMin = min(height[lo], height[hi])
            trapped += max(0, globalHigh-curMin)
            if height[lo] <= height[hi]:
                lo += 1
            else:
                hi -= 1
            globalHigh = max(globalHigh, curMin)
        return trapped

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
