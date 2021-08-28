from typing import Any

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
        def decode(strData: str) -> Any:
            nonlocal data
            data = strData
            if data[0] == '#':
                return None
            root = TreeNode(int(data[:data.find(',')]))
            root.left = decode(data[data.find(',')+1:])
            root.right = decode(data[data.find(',')+1:])
            return root
        return decode(data)

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
