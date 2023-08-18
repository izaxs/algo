# 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Constraints:

#     The number of nodes in the tree is in the range [0, 104].
#     -100 <= Node.val <= 100

import include
from binarytree import TreeNode, Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        stack: list[tuple[TreeNode, int]] = []
        curDepth, maxDepth = 0, 0
        while root:
            curDepth += 1
            maxDepth = max(maxDepth, curDepth)
            if root.right:
                stack.append((root.right, curDepth))
            if root.left:
                root = root.left
            elif stack:
                root, curDepth = stack.pop()
            else:
                break
        return maxDepth