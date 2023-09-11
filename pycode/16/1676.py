# 1676. Lowest Common Ancestor of a Binary Tree IV

# Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

# Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.

# Constraints:

#     The number of nodes in the tree is in the range [1, 104].
#     -109 <= Node.val <= 109
#     All Node.val are unique.
#     All nodes[i] will exist in the tree.
#     All nodes[i] are distinct.

import include
from binarytree import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: list[TreeNode]) -> TreeNode:
        targets = set(nodes)
        remained = len(nodes)
        def traverse(root: TreeNode | None) -> TreeNode | None:
            nonlocal remained
            if not root or not remained: return None
            current = False
            if root in targets:
                remained -= 1
                current = True
            a, b = traverse(root.left), traverse(root.right)
            if (a and b) or current: return root
            return a or b
        node = traverse(root)
        assert node
        return node
    
    def lowestCommonAncestor2(self, root: TreeNode, nodes: list[TreeNode]) -> TreeNode:
        nodeSet = set(nodes)
        def traverse(root: TreeNode | None) -> TreeNode | None:
            if not root or root in nodeSet: return root
            a, b = traverse(root.left), traverse(root.right)
            return root if a and b else a or b
        lca = traverse(root) or root
        return lca