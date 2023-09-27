import include
from binarytree import Optional, TreeNode

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack: list[TreeNode] = []
        self.cur = root

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration()
        self.cur = self.stack[-1].right
        return self.stack.pop().val

    def hasNext(self) -> bool:
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        if self.stack: return True
        return False
    
class BSTIterator2:

    def __init__(self, root: Optional[TreeNode]):
        self.stk: list[TreeNode] = []
        self._push(root)

    def _push(self, root):
        while root:
            self.stk.append(root)
            root = root.left

    def next(self) -> int:
        nextNode = self.stk.pop()
        result = nextNode.val
        self._push(nextNode.right)
        return result
        

    def hasNext(self) -> bool:
        return len(self.stk) > 0
