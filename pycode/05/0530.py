# 530. Minimum Absolute Difference in BST

# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Constraints:

#     The number of nodes in the tree is in the range [2, 104].
#     0 <= Node.val <= 105
import include
from binarytree import TreeNode, Optional

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        diff = (1 << 32) - 1
        def traverse(root: TreeNode) -> tuple[int, int]:
            nonlocal diff
            minVal, maxVal = root.val, root.val
            if root.left: 
                minVal, preVal = traverse(root.left)
                diff = min(diff, root.val-preVal)
            if root.right:
                nextVal, maxVal = traverse(root.right)
                diff = min(diff, nextVal-root.val)
            return minVal, maxVal
        if not root: return 0
        traverse(root)
        return diff

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        pre, diff = (-1) << 32, (1 << 32) - 1
        def traverse(node: TreeNode):
            nonlocal pre, diff
            if node.left: traverse(node.left)
            pre, diff = node.val, min(diff, node.val-pre)
            if node.right: traverse(node.right)
        if root: traverse(root)
        return diff
            