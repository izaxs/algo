# 617. Merge Two Binary Trees

# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import include
from binarytree import TreeNode, Optional, makeTree

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None
        val = 0
        left1 = right1 = left2 = right2 = None
        if root1:
            val += root1.val
            left1 = root1.left
            right1 = root1.right
        if root2:
            val += root2.val
            left2 = root2.left
            right2 = root2.right
        leftNode = self.mergeTrees(left1, left2)
        rightNode = self.mergeTrees(right1, right2)
        return TreeNode(val, leftNode, rightNode)
        

if __name__ == '__main__':
    null = None
    root1 = makeTree([1,3,2,5])
    root2 = makeTree([2,1,3,null,4,null,7])
    s = Solution()
    s.mergeTrees(root1, root2)