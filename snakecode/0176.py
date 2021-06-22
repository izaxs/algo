# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from util.linkedlist import ListNode
from typing import Optional

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
