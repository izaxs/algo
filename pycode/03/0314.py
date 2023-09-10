# Binary Tree Vertical Order Traversal

# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Constraints:

#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100

import include
from binarytree import TreeNode, Optional, makeTree
from collections import deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        def getRange(root: Optional[TreeNode], lo: int, hi: int) -> tuple[int, int]:
            if not root: return lo + 1, hi - 1
            leftLo, leftHi = getRange(root.left, lo - 1, hi - 1)
            rightLo, rightHi = getRange(root.right, lo + 1, hi + 1)
            return min(leftLo, rightLo), max(leftHi, rightHi)
        if not root: return []
        lowest, highest = getRange(root, 0, 0)
        cols = [[] for _ in range(highest - lowest + 1)]
        dq: deque[tuple[int, TreeNode]] = deque([(0, root)])
        while dq:
            size = len(dq)
            for _  in range(size):
                order, node = dq.popleft()
                cols[order - lowest].append(node.val)
                if node.left: dq.append((order - 1, node.left))
                if node.right: dq.append((order + 1, node.right))
        return cols
    
    def verticalOrder2(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root: return []
        seen: dict[int, list[int]] = {}
        queue: deque[tuple[int, TreeNode]] = deque([(0, root)])
        lo, hi = 0, 0
        while queue:
            order, node = queue.popleft()
            lo, hi = min(lo, order), max(hi, order)
            seen.setdefault(order, []).append(node.val)
            if node.left: queue.append((order - 1, node.left))
            if node.right: queue.append((order + 1, node.right))
        return [seen[i] for i in range(lo, hi + 1)]
            
    
if __name__ == '__main__':
    null = None

    values = [3,9,8,4,0,1,7,null,null,null,2,5]
    root = makeTree(values)
    result = Solution().verticalOrder2(root)
    print(result)
        
        