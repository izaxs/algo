import include
from util.binarytree import Optional, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.min = -1 << 32
        _, res = self.helper(root)
        return res

    def helper(self, root: Optional[TreeNode]) -> tuple[int, int]: # topDownPathMax, curMax
        if not root: return (self.min, self.min)
        leftDown, leftMax = self.helper(root.left)
        rightDown, rightMax = self.helper(root.right)
        leftDown, rightDown = max(leftDown, 0), max(rightDown, 0)
        maxDown = max(leftDown, rightDown)+root.val
        maxPath = max(leftDown+rightDown+root.val, max(leftMax, rightMax))
        return (maxDown, maxPath)
