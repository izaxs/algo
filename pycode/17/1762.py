# Buildings With an Ocean View

# There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

# Constraints:

#     1 <= heights.length <= 105
#     1 <= heights[i] <= 109

class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        result: list[int] = [] 
        maxHeight = 0
        for i in reversed(range(0, len(heights))):
            if (h := heights[i]) <= maxHeight: continue
            result.append(i)
            maxHeight = h
        return list(reversed(result))

