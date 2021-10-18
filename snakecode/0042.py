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

    def trap2(self, height: list[int]) -> int:
        wall, bot = 0, 0
        lo, hi = 0, len(height)-1
        trapped = 0
        while lo < hi:
            hLo, hHi = height[lo], height[hi]
            if hLo < hHi:
                bot = hLo
                wall = max(wall, hLo)
                lo += 1
            else:
                bot = hHi
                wall = max(wall, hHi)
                hi -= 1
            trapped += max(0, wall-bot)
        return trapped

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
