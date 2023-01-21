"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, val: bool, isLeaf: bool, topLeft: Optional[Node], topRight: Optional[Node], bottomLeft: Optional[Node], bottomRight: Optional[Node]):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        n = len(grid)

        def subTree(xLo: int, xHi: int, yLo: int, yHi: int) -> Node:
            if xLo == xHi:
                return Node(bool(grid[xLo][yLo]), True, None, None, None, None)
            xMid, yMid = (xLo+xHi)//2, (yLo+yHi)//2
            topLeft = subTree(xLo, xMid, yLo, yMid)
            topRight = subTree(xLo, xMid, yMid+1, yHi)
            bottomLeft = subTree(xMid+1, xHi, yLo, yMid)
            bottomRight = subTree(xMid+1, xHi, yMid+1, yHi)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
                if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                    return topLeft
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return subTree(0, n-1, 0, n-1)
