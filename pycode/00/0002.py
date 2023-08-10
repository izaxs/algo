# Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Constraints:

#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.


import include
from linkedlist import Optional, ListNode, linkerize

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
    
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fake, carry = ListNode(), 0
        cur = fake
        while l1 or l2 or carry:
            if l1: 
                carry += l1.val
                l1 = l1.next
            if l2: 
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            carry //= 10
            cur = cur.next
        return fake.next


if __name__ == '__main__':
    s = Solution()
    l1 = linkerize([0, 1, 2, 3])
    l2 = linkerize([5, 9, 7, 3, 4])
    print(s.addTwoNumbers(l1, l2))

    l1 = linkerize([2, 4, 3])
    l2 = linkerize([5, 6, 4])
    print(s.addTwoNumbers(l1, l2))
