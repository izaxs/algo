from typing import List

class ListNode:
    ''' Node for singly-linked list '''
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(listize(self))
        
def linkerize(nums: List) -> ListNode:
    ''' Convert Python list to singly-linked list '''
    fake = ListNode()
    pre = fake
    for v in nums:
        pre.next = ListNode(v)
        pre = pre.next
    return fake.next

def listize(head: ListNode) -> List:
    ''' Convert singly-linked list to Python list '''
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result