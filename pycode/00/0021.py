# Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Constraints:

#     The number of nodes in both lists is in the range [0, 50].
#     -100 <= Node.val <= 100
#     Both list1 and list2 are sorted in non-decreasing order.


import include
from linkedlist import Optional, ListNode, linkerize, listize


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode()
        cur = fake
        while True:
            if list1:
                if list2 and list2.val < list1.val:
                    list1, list2 = list2, list1
            else:
                list1, list2 = list2, list1
            if list1:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                break
        return fake.next

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = fake = ListNode()
        while list1 and list2:
            if list1.val >= list2.val:
                list1, list2 = list2, list1
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        cur.next = list1 if list1 else list2
        return fake.next

    def mergeTwoLists3(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

if __name__ == "__main__":
    s = Solution()
    l1 = linkerize([2, 6, 8, 9, 20])
    l2 = linkerize([0, 3, 5, 6, 7, 11, 15])
    m = s.mergeTwoLists2(l1, l2)
    print(listize(m))

