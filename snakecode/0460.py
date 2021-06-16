from typing import Optional

class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key: int = key
        self.val: int = val
        self.freq: int = 0
        self.pre: Optional[Node] = None
        self.next: Optional[Node] = None

class DLList:
    def __init__(self):
        self.size = 0
        self._guard = Node()
        self._guard.pre = self._guard.next = self._guard

    def headify(self, node: Optional[Node]):
        node.pre = self._guard
        node.next = self._guard.next
        node.next.pre = node
        self._guard.next = node
        self.size += 1

    def pop(self, node: Optional[Node] = None):
        if self.size == 0:
            return
        if not node:
            node = self._guard.pre
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre, node.next = None, None
        self.size -= 1
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self._groups: dict[int, DLList] = {}
        self._nodes: dict[int, Node] = {}
        self._cap = capacity
        self._size = 0
        self._minFreq = 1

    def get(self, key: int) -> int:
        '''Get Node, update Cache and Node status'''
        if key not in self._nodes:
            return -1
        node = self._nodes[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int):
        '''
        If it's a existing Node, update Cache and Node.\n
        If it's a new Node and there're space, update Cache.\n
        If it's a new Node but no space, kick out one Node, update Cache
        '''
        if self._cap == 0:
            return
        if key in self._nodes:
            node = self._nodes[key]
            node.val = value
        else:
            node = Node(key, value)
            if self._size < self._cap:
                self._addNew(node)
            else:
                self._addNew(node, kick=True)
        self._update(node)

    def _update(self, node: Node):
        '''Given a Node in cache, update it's freq and cache status'''
        group = self._groups[node.freq]
        group.pop(node)
        groupNext = self._getGroup(node.freq+1)
        groupNext.headify(node)
        if node.freq == self._minFreq and group.size == 0:
            self._minFreq = node.freq + 1
        node.freq += 1

    def _addNew(self, node: Node, kick: bool = False):
        '''
        Simply kickout the least frequently used Node from frequency group and node map\n
        Replace it with a new Node, set cache min frequency to 1
        '''
        if self._cap == 0:
            return
        if kick:
            group = self._getGroup(self._minFreq)
            badNode = group.pop()
            self._nodes.pop(badNode.key)
            self._size -= 1
        self._minFreq = node.freq = 0
        self._getGroup(node.freq).headify(node)
        self._nodes[node.key] = node
        self._size += 1

    def _getGroup(self, freq: int) -> DLList:
        return self._groups.setdefault(freq, DLList())


def test(actions: list[str], val: list):
    cache: Optional[LFUCache] = None
    result: list = []
    for i, v in zip(actions, val):
        if i == 'LFUCache':
            cache = LFUCache(v[0])
            result.append(None)
        elif i == 'put':
            result.append((i, v, cache.put(v[0], v[1])))
        elif i == 'get':
            result.append((i, v, cache.get(v[0])))
    print(result)

actions = ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
values = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
test(actions, values)

# actions2 = ["LFUCache","put","put","get","get","get","put","put","get","get","get","get"]
# values2 = [[3],[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]
# test(actions2, values2)

# actions3 = ["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
# values3 = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
# test(actions3, values3)