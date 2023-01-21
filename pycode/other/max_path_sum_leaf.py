from __future__ import annotations
import include
from binarytree import Optional, TreeNode

class Path:
    def __init__(
        self,
        down: int = 0,
        cross: int = 0,
        other: Optional[Path] = None
    ) -> None:
        if other:
            self.down = other.down
            self.cross = other.cross
            self.downNodes: list[TreeNode] = other.downNodes[:]
            self.crossNodes: list[TreeNode] = other.crossNodes[:]
        else:
            self.down = down
            self.cross = cross
            self.downNodes: list[TreeNode] = []
            self.crossNodes: list[TreeNode] = []

    def __repr__(self) -> str:
        return f'P#d:{self.down} c:{self.cross} dn:{self.downNodes} cn:{self.crossNodes}#'

# Find nodes path with maximum sum between two leaf nodes
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> tuple[int, list[TreeNode]]:
        self.min = -1 << 32
        path = self.helper(root)
        return path.cross, path.crossNodes

    def helper(self, root: Optional[TreeNode]) -> Path:
        cur = Path(self.min, self.min)
        if not root: return cur
        if not root.left and not root.right:
            cur.down, cur.downNodes = root.val, [root]
            return cur
        left = self.helper(root.left)
        right = self.helper(root.right)
        cur.down = (left.down if left.down > right.down else right.down)+root.val
        cur.downNodes = (left.downNodes if left.down > right.down else right.downNodes)[:]
        cur.downNodes.append(root)
        if cur.cross < left.cross:
            cur.cross = left.cross
            cur.crossNodes = left.crossNodes
        if cur.cross < right.cross:
            cur.cross = right.cross
            cur.crossNodes = right.crossNodes
        crossNow = left.down+right.down+root.val
        if left.down != self.min and right.down != self.min and cur.cross < crossNow:
            cur.cross = crossNow
            cur.crossNodes = left.downNodes+[root]+right.downNodes[::-1]
        # print(f'At: {root.val}, return: {cur}')
        return cur

#          2
#     29       1
# -29        5   6
#         -10 -12
n0 = TreeNode(2)
n1, n3 = TreeNode(29), TreeNode(1)
n2, n4, n5 = TreeNode(-29), TreeNode(5), TreeNode(6)
n6, n7 = TreeNode(-10), TreeNode(-2)

n0.left, n0.right = n1, n3
n1.left, n3.left, n3.right = n2, n4, n5
n4.left, n4.right = n6, n7

s = Solution()
print(s.maxPathSum(n0))
