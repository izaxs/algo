import include
from linkedlist import Optional, ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            assert slow
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
