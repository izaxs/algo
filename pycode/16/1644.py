# 1644. Lowest Common Ancestor of a Binary Tree II

# Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

# Constraints:

#     The number of nodes in the tree is in the range [1, 104].
#     -109 <= Node.val <= 109
#     All Node.val are unique.
#     p != q

import include
from binarytree import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
        foundP, foundQ = False, False
        def traverse(root: TreeNode | None) -> TreeNode | None:
            nonlocal foundP, foundQ
            if not root or (foundP and foundQ): return None
            found = None
            if root == p: 
                foundP = True
                found = p
            if root == q: 
                foundQ = True
                found = q
            a, b = traverse(root.left), traverse(root.right)
            return root if a and b else found if found else a if a else b
        result = traverse(root)
        return result if foundP and foundQ else None

