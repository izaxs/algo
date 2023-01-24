# N-ary Tree Preorder Traversal
# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# 0 <= Node.val <= 104
# The height of the n-ary tree is less than or equal to 1000.

import include
from narytree import Optional, NTreeNode as Node

class Solution:
    def preorder(self, root: Optional[Node]) -> list[int]:
        if not root:
            return []
        res = [root.val]
        for child in root.children:
            res += self.preorder(child)
        return res

    def preorder2(self, root: Optional[Node]) -> list[int]:
        if not root:
            return []
        res: list[int] = []
        stack: list[Node] = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack += reversed(cur.children) if cur.children else []
        return res

    # The Pythonic Way
    def preorder3(self, root: Optional[Node]) -> list[int]:
        def traversal(stack: list[Node]):
            while stack:
                cur = stack.pop()
                yield cur.val
                if cur.children:
                    stack += reversed(cur.children)
        return list(traversal([root])) if root else []





