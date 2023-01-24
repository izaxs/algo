# Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

import include
from binarytree import Optional, TreeNode
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        dq = deque([root])
        res: list[list[int]] = []
        while dq:
            subList = []
            for _ in range(len(dq)):
                cur = dq.popleft()
                subList.append(cur.val)
                dq.append(cur.left) if cur.left else None
                dq.append(cur.right) if cur.right else None
            res.append(subList)
        return res

    def levelOrder2(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        res, level = [], [root]
        while level:
            res.append([n.val for n in level])
            level = [sub for n in level for sub in (n.left, n.right) if sub]
        return res
