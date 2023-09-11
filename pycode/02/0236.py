# 236. Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Constraints:

#     The number of nodes in the tree is in the range [2, 105].
#     -109 <= Node.val <= 109
#     All Node.val are unique.
#     p != q
#     p and q will exist in the tree.

# Definition for a binary tree node.
import include
from binarytree import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(root: TreeNode | None) -> TreeNode | None:
            if not root: return None
            if root == p or root == q: return root
            a, b = traverse(root.left), traverse(root.right)
            return root if a and b else a if a else b
        res = traverse(root)
        assert res
        return res
