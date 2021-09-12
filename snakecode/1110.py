from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        def helper(cur: Optional[TreeNode]) -> Optional[TreeNode]:
            if cur is None:
                return None
            cur.left = helper(cur.left)
            cur.right = helper(cur.right)
            if cur.val in toD:
                if cur.left: res.append(cur.left)
                if cur.right: res.append(cur.right)
                return None
            return cur

        res: list[TreeNode] = []
        toD = set(to_delete)
        curRoot = helper(root)
        if curRoot: res.append(curRoot)
        return res