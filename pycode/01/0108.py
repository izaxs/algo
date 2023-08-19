# 108. Convert Sorted Array to Binary Search Tree

# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Constraints:

#     1 <= nums.length <= 104
#     -104 <= nums[i] <= 104
#     nums is sorted in a strictly increasing order.
import include
from binarytree import TreeNode, Optional

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def makeTree(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi: return None
            mid = (lo + hi) >> 1
            root = TreeNode(nums[mid])
            root.left = makeTree(lo, mid-1)
            root.right = makeTree(mid+1, hi)
            return root
        root = makeTree(0, len(nums)-1)
        return root
