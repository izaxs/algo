from typing import Optional

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.pre: Optional[Node] = None
        self.next: Optional[Node] = None

class LRUCache:
    def __init__(self, cap: int):
        self._guard: Node = Node(0, 0)
        self._guard.pre = self._guard
        self._guard.next = self._guard
        self._nodes: dict[int, Node] = {}
        self._cap = cap

    def _extract(self, key: int) -> Node:
        node = self._nodes[key]
        preNode, nextNode = node.pre, node.next
        assert preNode
        preNode.next = nextNode
        assert nextNode
        nextNode.pre = preNode
        return node

    def _pushFront(self, node: Node):
        nextNode = self._guard.next
        assert nextNode
        self._guard.next = node
        nextNode.pre = node
        node.next = nextNode
        node.pre = self._guard

    def get(self, key: int) -> int:
        if key not in self._nodes:
            return -1
        node = self._extract(key)
        self._pushFront(node)
        return node.val

    def put(self, key: int, val: int):
        if key not in self._nodes:
            node = Node(key, val)
            self._nodes[key] = node
        else:
            node = self._extract(key)
            node.val = val
        self._pushFront(node)
        if len(self._nodes) > self._cap:
            toRemove = self._guard.pre
            assert toRemove
            self._extract(toRemove.key)
            del self._nodes[toRemove.key]
