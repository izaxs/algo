class Node:
    def __init__(self, isLeaf: bool = False) -> None:
        self.children: dict[str, Node] = {}
        self.isLeaf = isLeaf

class Trie:
    def __init__(self):
        self.root = Node()

    def _put(self, word: str, curIndex: int, preNode: Node) -> None:
        if curIndex >= len(word): return
        isLeaf = True if curIndex == len(word)-1 else False
        curNode = preNode.children.setdefault(word[curIndex], Node(isLeaf))
        if isLeaf: curNode.isLeaf = isLeaf
        self._put(word, curIndex+1, curNode)

    def insert(self, word: str) -> None:
        self._put(word, 0, self.root)

    def search(self, word: str) -> bool:
        curNode = self.root
        fakeNode = Node()
        for c in word:
            curNode = curNode.children.get(c, fakeNode)
            if curNode is fakeNode: return False
        return curNode.isLeaf

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        fakeNode = Node()
        for c in prefix:
            curNode = curNode.children.get(c, fakeNode)
            if curNode is fakeNode: return False
        return True
