from __future__ import annotations
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'TN:{self.val}'

# Make a tree using LeetCode TreeNode test case format
def makeTree(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] == None: return None
    root = TreeNode(values[0])
    dq = deque([root])
    i = 1
    while dq:
        size = len(dq)
        for _ in range(size):
            parent = dq.popleft()
            if i == len(values): return root
            if (v := values[i]) != None:
                parent.left = TreeNode(v)
                dq.append(parent.left)
            i += 1
            if i == len(values): return root
            if (v := values[i]) != None:
                parent.right = TreeNode(v)
                dq.append(parent.right)
            i += 1
    return root

def printPreOrder(root: TreeNode | None):
    seq: list[int] = []
    preOrder(root, seq)
    print(seq)

def preOrder(root: TreeNode | None, seq: list[int]):
    if not root: return
    seq.append(root.val)
    preOrder(root.left, seq)
    preOrder(root.right, seq)
    