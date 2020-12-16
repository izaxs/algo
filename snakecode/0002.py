from lib.linkedlist import ListNode, linkerize

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode()
    pre = head
    carry = 0
    while l1 or l2:
        cur = ListNode(carry)
        if l1:
            cur.val += l1.val
            l1 = l1.next
        if l2:
            cur.val += l2.val
            l2 = l2.next
        carry = cur.val // 10
        cur.val = cur.val % 10
        pre.next = cur
        pre = cur
    if carry > 0:
        pre.next = ListNode(1)
    return head

l1 = linkerize([0, 1, 2, 3])
l2 = linkerize([5, 9, 7, 3, 4])
result = addTwoNumbers(l1, l2)
print(result)

