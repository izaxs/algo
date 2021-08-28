from typing import Any
from collections import deque

# Definition for a binary tree node.
class TreeNode():
    def __init__(self, x: Any):
        self.val = x
        self.left: Any = None
        self.right: Any = None


class Codec:
    def serialize(self, root: Any):
        def encode(root: Any) -> str:
            if root is None:
                return '#'
            return f'{root.val},{encode(root.left)},{encode(root.right)}'
        res = encode(root)
        return res

    def deserialize(self, data: str):
        def decode(data: deque[str]) -> Any:
            val = data.popleft()
            if val == '#':
                return
            root = TreeNode(int(val))
            root.left = decode(data)
            root.right = decode(data)
            return root
        queue = deque(data.split(','))
        return decode(queue)

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.right = n2
n2.left = n3
n2.right = n4

code = '1,#,2,3,#,#,4,#,#'
encoded = Codec().serialize(n1)
decoded = Codec().deserialize(encoded)
