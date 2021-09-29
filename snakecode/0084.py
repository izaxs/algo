class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        stack: list[int] = [-1]
        ans = 0
        for i, h in enumerate(heights):
            while stack and h <= heights[stack[-1]]:
                curH = heights[stack.pop()]
                if not stack: break
                curW = i-stack[-1]-1
                ans = max(ans, curW*curH)
            stack.append(i)
        return ans