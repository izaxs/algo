# 637. Average of Levels in Binary Tree

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted. 

# Constraints:

#     The number of nodes in the tree is in the range [1, 104].
#     -231 <= Node.val <= 231 - 1

import include
from binarytree import TreeNode, Optional
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        res: list[float] = []
        dq: deque[TreeNode] = deque()
        if root: dq.append(root)
        while dq:
            size, valSum = len(dq), 0
            for i in range(size):
                node = dq.pop()
                valSum += node.val
                if node.right: dq.appendleft(node.right)
                if node.left: dq.appendleft(node.left)
            res.append(valSum/size)
        return res