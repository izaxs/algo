import include
from util.linkedlist import Optional, ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curNode = None
        nextNode = head
        while nextNode:
            farNode = nextNode.next
            nextNode.next = curNode
            curNode = nextNode
            nextNode = farNode
        assert curNode
        return curNode

    def reverseList2(self, head: ListNode) -> ListNode:
        tail = self.reverseNode(head, None)
        assert tail
        return tail

    def reverseNode(self, curNode: Optional[ListNode], preNode: Optional[ListNode]) -> Optional[ListNode]:
        if not curNode:
            return preNode
        nextNode = curNode.next
        curNode.next = preNode
        return self.reverseNode(nextNode, curNode)
