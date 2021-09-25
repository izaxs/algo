# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional[ListNode] = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False