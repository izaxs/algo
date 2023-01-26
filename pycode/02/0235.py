# Lowest Common Ancestor of a Binary Search Tree

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Constraints:

#     The number of nodes in the tree is in the range [2, 105].
#     -109 <= Node.val <= 109
#     All Node.val are unique.
#     p != q
#     p and q will exist in the BST.

from binarytree import Optional, TreeNode

class Solution:
    # Forgot the tree is BST!!!
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(cur: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
            if not cur:
                return None
            seen = cur if cur == p or cur == q else None
            if seen:
                return seen
            for n in (cur.left, cur.right):
                n = search(n, p, q)
                if n:
                    if n != p and n != q:
                        return n
                    if seen:
                        return cur
                    seen = n
            return seen

        res = search(root, p, q)
        assert res
        return res

    # Forgot the tree is BST!!!
    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(cur: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
            if not cur:
                return None
            if cur == p or cur == q:
                return cur
            left = search(cur.left, p, q)
            if left and left != p and left != q:
                return left
            right = search(cur.right, p, q)
            if right and right != p and right != q:
                return right
            if left and right:
                return cur
            if not left and not right:
                return None
            return left if left else right
        res = search(root, p, q)
        assert res
        return res

    def lowestCommonAncestor3(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p, q = (q, p) if q.val <= p.val else (p, q)
        while not (p.val <= root.val <= q.val):
            if root.val < p.val:
                assert root.right
                root = root.right
            else:
                assert root.left
                root = root.left
        return root

    # Non-typed short version
    def lowestCommonAncestor4(self, root, p, q):
        p, q = (q, p) if q.val <= p.val else (p, q)
        while not (p.val <= root.val <= q.val):
            root = root.right if root.val < p.val else root.left
        return root
            
            