# Palindrome Linked List

# Given the head of a singly linked list, return true if it is a
# palindrome or false otherwise.

# Constraints:

#     The number of nodes in the list is in the range [1, 105].
#     0 <= Node.val <= 9

 
# Follow up: Could you do it in O(n) time and O(1) space?
import include
from linkedlist import Optional, ListNode

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fake = ListNode(next=head)
        # find midway node
        slow = fast = fake
        while fast.next and fast.next.next:
            assert slow
            slow = slow.next
            fast = fast.next.next
        # reverse
        assert slow
        forwardEnd, backwardEnd = slow, slow.next
        pre, cur = slow, slow.next
        while cur:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode
        # two pointers move to mid
        forward, backward = fake.next, pre
        while True:
            assert forward and backward
            if forward.val != backward.val: return False
            if forward == forwardEnd or backward == backwardEnd: break
            forward, backward = forward.next, backward.next
        return True
        
if __name__ == "__main__":
    from linkedlist import linkerize
    nodes = [1, 2, 2, 1]
    linkedNodes = linkerize(nodes)
    r = Solution().isPalindrome(linkedNodes)        
    print(r)
