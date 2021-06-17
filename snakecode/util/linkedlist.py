from __future__ import annotations
from typing import Optional, Any

class ListNode:
    ''' Node for singly-linked list '''
    def __init__(self, val: Any = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(listize(self))

def linkerize(items: list[Any]) -> Optional[ListNode]:
    ''' Convert Python list to singly-linked list '''
    fake = ListNode()
    pre = fake
    for v in items:
        pre.next = ListNode(v)
        pre = pre.next
    return fake.next

def listize(head: Optional[ListNode]) -> list[ListNode]:
    ''' Convert singly-linked list to Python list '''
    result: list[Any] = []
    while head:
        result.append(head.val)
        head = head.next
    return result