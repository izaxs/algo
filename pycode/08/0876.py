# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import include
from linkedlist import Optional, ListNode

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = fast = head
        while fast and fast.next:
            assert mid
            mid = mid.next
            fast = fast.next.next
        return mid