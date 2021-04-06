class Node:
    def __init__(self, key: int, val: int, preNode = None, nextNode = None):
        self.key = key
        self.val = val
        self.pre, self.next = preNode, nextNode

class LRUCache:
    def __init__(self, capacity: int):
        self.guard = Node(-1, -1)
        self.guard.pre, self.guard.next = self.guard, self.guard
        self.lookup = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        curNode = self.lookup.get(key)
        if not curNode: return -1
        self._remove(curNode)
        self._add(curNode)
        return curNode.val

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0: return
        curNode = self.lookup.get(key)
        if curNode:
            curNode.val = value
            self._remove(curNode)
            self._add(curNode)
            return
        if len(self.lookup) == self.cap:
            evicted = self._remove(self.guard.pre)
            del self.lookup[evicted.key]
        curNode = Node(key, value)
        self.lookup[key] = curNode
        self._add(curNode)

    def _add(self, node: Node):
        node.pre, node.next = self.guard, self.guard.next
        self.guard.next.pre, self.guard.next = node, node
        pass

    def _remove(self, node: Node) -> Node:
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre, node.next = None, None
        return node

    def __str__(self) -> str:
        curNode = self.guard.next
        res = ''
        while curNode != self.guard:
            res += f'{curNode.key}:{curNode.val} '
            curNode = curNode.next
        return res

# Your LRUCache object will be instantiated and called as such:
def test1():
    obj = LRUCache(3)
    print(obj.get(1))
    obj.put(1,1)
    print(obj)
    obj.put(2,2)
    print(obj)
    obj.put(3,3)
    print(obj)
    print('get: ', obj.get(2))
    print(obj)
    obj.put(4,4)
    print(obj)

def test2():
    obj = LRUCache(2)
    obj.put(2,1)
    print(obj)
    obj.put(1,1)
    print(obj)
    obj.put(2,3)
    print(obj)
    obj.put(4,1)
    print(obj)

test2()