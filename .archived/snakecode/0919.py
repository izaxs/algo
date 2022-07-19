from typing import Optional
from collections import deque
from util.binarytree import TreeNode

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue: deque[TreeNode] = deque()
        if self.root:
            self.queue.append(self.root)
            while True:
                cur = self.queue.popleft()
                if cur.left and cur.right:
                    self.queue.append(cur.left)
                    self.queue.append(cur.right)
                else:
                    self.queue.appendleft(cur)
                    break

    def insert(self, val: int) -> int:
        if not self.root:
            self.root = TreeNode(val)
            self.queue.append(self.root)
            return -1
        parent = self.queue[0]
        newNode = TreeNode(val)
        if not parent.left:
            parent.left = newNode
        else:
            parent.right = newNode
            self.queue.popleft()
            self.queue.append(parent.left)
            self.queue.append(parent.right)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
