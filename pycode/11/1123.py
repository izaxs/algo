# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

# Recall that:

#     The node of a binary tree is a leaf if and only if it has no children
#     The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
#     The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

# Constraints:

#     The number of nodes in the tree will be in the range [1, 1000].
#     0 <= Node.val <= 1000
#     The values of the nodes in the tree are unique.

import include
from binarytree import Optional, TreeNode

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nullNode = TreeNode(0)
        def helper(node: TreeNode, depth: int) -> tuple[TreeNode, int]: # lca, depth
            if not node.left and not node.right:
                return node, depth
            leftLca, leftDepth = helper(node.left, depth + 1) if node.left else (nullNode, 0)
            rightLca, rightDepth = helper(node.right, depth + 1) if node.right else (nullNode, 0)
            if leftDepth == rightDepth:
                return node, leftDepth
            if leftDepth > rightDepth:
                return leftLca, leftDepth
            else:
                return rightLca, rightDepth
        if not root: return None
        node, _ = helper(root, 0)
        return node
            