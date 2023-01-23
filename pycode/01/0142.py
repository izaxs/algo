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

    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Utilize fake head
        if not head:
            return None
        fake = ListNode()
        fake.next = head
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return None
            assert slow
            slow = slow.next
            fast = fast.next.next
        slow = fake
        while slow != fast:
            assert slow and fast
            slow = slow.next
            fast = fast.next
        return slow

    def detectCycle3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def tryMeet(head: Optional[ListNode]) -> Optional[ListNode]:
            slow = fast = head
            while fast and fast.next:
                assert slow
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return fast
            return None
        
        meet = tryMeet(head)
        if not meet:
            return None
        while head != meet:
            assert head and meet
            head, meet = head.next, meet.next
        return head