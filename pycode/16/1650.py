# 1650. Lowest Common Ancestor of a Binary Tree III

# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

# Each node will have a reference to its parent node. The definition for Node is below:

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

# Constraints:

#     The number of nodes in the tree is in the range [2, 105].
#     -109 <= Node.val <= 109
#     All Node.val are unique.
#     p != q
#     p and q exist in the tree.

class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        seen: set[int] = set()
        def goUp(a: Node | None, b: Node | None) -> Node:
            if a == q: return q
            if b == p: return p
            if a:
                if a.val in seen: return a
                seen.add(a.val)
            pa = a.parent if a else None
            if b:
                if b.val in seen: return b
                seen.add(b.val)
            pb = p.parent if a else None
            return goUp(pa, pb)
        return goUp(p, q)
    
    def lowestCommonAncestor2(self, p: Node, q: Node) -> Node:
        a, b = p, q
        while a != b:
            a = a.parent if a.parent else q
            b = b.parent if b.parent else p
        return a

            

        
