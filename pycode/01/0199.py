# 199. Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Constraints:

#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100

import include
from binarytree import TreeNode, Optional
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root: return []
        result: list[int] = []
        level: deque[TreeNode] = deque([root])
        while level:
            size = len(level)
            result.append(level[0].val)
            for _ in range(size):
                cur = level.popleft()
                if cur.right: level.append(cur.right)
                if cur.left: level.append(cur.left)
        return result
    
    def rightSideView2(self, root: Optional[TreeNode]) -> list[int]:
        views: list[int] = []
        def traversal(root: TreeNode | None, depth: int):
            if not root: return
            if depth == len(views): views.append(root.val)
            traversal(root.right, depth + 1)
            traversal(root.left, depth + 1)
        traversal(root, 0)
        return views
                
        
        