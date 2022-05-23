# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
from util.linkedlist import ListNode

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        hasCycle = False
        while fast and fast.next and not hasCycle:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
        if not hasCycle: return None
        while head != fast:
            head = head.next
            fast = fast.next
        return head
