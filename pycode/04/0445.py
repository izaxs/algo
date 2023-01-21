import include
from linkedlist import Optional, ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1: list[int] = []
        s2: list[int] = []
        while l1 is not None:
            s1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            s2.append(l2.val)
            l2 = l2.next
        curNode: Optional[ListNode] = None
        carry = 0
        while s1 or s2 or carry:
            if s1: carry += s1.pop()
            if s2: carry += s2.pop()
            curNode = ListNode(carry % 10, curNode)
            carry //= 10
        return curNode
