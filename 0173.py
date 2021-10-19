from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack: list[TreeNode] = []
        self.cur = root

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration()
        self.cur = self.stack[-1].right
        return self.stack.pop().val

    def hasNext(self) -> bool:
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        if self.stack: return True
        return False
                
        