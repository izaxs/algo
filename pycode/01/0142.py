import include
from linkedlist import Optional, ListNode

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        hasCycle = False
        while fast and fast.next and not hasCycle:
            assert slow
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
        if not hasCycle: return None
        while head != fast:
            assert head and fast
            head = head.next
            fast = fast.next
        return head
