# Validate Binary Search Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1



import include
from binarytree import Optional, TreeNode
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(cur: Optional[TreeNode], lo: Optional[int], hi: Optional[int]) -> bool:
            if not cur:
                return True
            if (lo != None and cur.val <= lo) or (hi != None and cur.val >= hi):
                return False
            return validate(cur.left, lo, cur.val) and validate(cur.right, cur.val, hi)
        return validate(root, None, None)

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        def validate(cur: Optional[TreeNode], lo = -math.inf, hi = math.inf) -> bool:
            if not cur:
                return True
            if not (lo < cur.val < hi):
                return False
            return validate(cur.left, lo, cur.val) and validate(cur.right, cur.val, hi)
        return validate(root)