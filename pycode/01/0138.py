# 138. Copy List with Random Pointer

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

#     val: an integer representing Node.val
#     random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

# Your code will only be given the head of the original linked list.

# Constraints:

#     0 <= n <= 1000
#     -104 <= Node.val <= 104
#     Node.random is null or is pointing to some node in the linked list.

# Definition for a Node.
from __future__ import annotations

class Node:
    def __init__(self, x: int, next: Node | None = None, random: Node | None = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        if not head: return None
        # Insert without random
        cur = head
        while cur:
            nextNode = cur.next
            insertNode = Node(cur.val, nextNode)
            cur.next = insertNode
            cur = nextNode
        
        # Link random
        cur = head
        while cur:
            newRandomNode = cur.random.next if cur.random else None
            assert cur.next
            cur.next.random = newRandomNode
            cur = cur.next.next if cur.next else None
        
        # detach new list
        newHead = head.next
        cur = newHead
        while cur:
            newNextNode = cur.next.next if cur.next else None
            cur.next = newNextNode
            cur = newNextNode

        return newHead
            
