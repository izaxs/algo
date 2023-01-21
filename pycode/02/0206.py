import include
from linkedlist import Optional, ListNode, linkerize, listize

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre: Optional[ListNode] = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return tail

if __name__ == "__main__":
    s = Solution()
    ll = linkerize([1, 2, 3, 4, 5])
    r1 = s.reverseList(ll)
    print(listize(r1))
    r2 = s.reverseList2(r1)
    print(listize(r2))

    

