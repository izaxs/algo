# 938. Range Sum of BST

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Constraints:

#     The number of nodes in the tree is in the range [1, 2 * 104].
#     1 <= Node.val <= 105
#     1 <= low <= high <= 105
#     All Node.val are unique.

import include
from binarytree import TreeNode, Optional

class Solution:
    def rangeSumBST0(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rangeSum = 0
        def traverse(node: TreeNode | None):
            if not node: return
            nonlocal rangeSum
            if node.val >= low:
                traverse(node.left)
            if node.val <= high:
                traverse(node.right)
            if low <= node.val <= high:
                rangeSum += node.val
        traverse(root)
        return rangeSum
            
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root : return 0
        rangeSum = root.val if low <= root.val <= high else 0
        if root.val >= low: rangeSum += self.rangeSumBST(root.left, low, high)
        if root.val <= high: rangeSum += self.rangeSumBST(root.right, low, high)
        return rangeSum
        
        

        