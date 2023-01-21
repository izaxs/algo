import include
from util.linkedlist import Optional, ListNode, linkerize

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        pre = head
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            pre.next = ListNode(val)
            pre = pre.next
        return head.next

if __name__ == '__main__':
    s = Solution()
    l1 = linkerize([0, 1, 2, 3])
    l2 = linkerize([5, 9, 7, 3, 4])
    print(s.addTwoNumbers(l1, l2))

    l1 = linkerize([2, 4, 3])
    l2 = linkerize([5, 6, 4])
    print(s.addTwoNumbers(l1, l2))
