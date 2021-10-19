from __future__ import annotations
from typing import Optional

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return True

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return 0

    def getList(self) -> list[NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return []

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.stack = nestedList[::-1]
        self.nextInt: Optional[int] = None

    def next(self) -> int:
        if not self.hasNext(): raise StopIteration()
        assert self.nextInt is not None
        res = self.nextInt
        self.nextInt = None
        return res

    def hasNext(self) -> bool:
        if not self.stack and self.nextInt is None: return False
        if self.nextInt is not None: return True
        while self.stack:
            cur = self.stack.pop()
            if cur.isInteger():
                self.nextInt = cur.getInteger()
                return True
            nextList = cur.getList()
            self.stack.extend(nextList[::-1])
        return False

class NestedIterator2:
    def __init__(self, nestedList: list[NestedInteger]):
        self.stk = nestedList[::-1]

    def next(self) -> int:
        return self.stk.pop().getInteger()

    def hasNext(self) -> bool:
        if not self.stk: return False
        val = self.stk[-1]
        if val.isInteger(): return True
        valList = val.getList()
        self.stk.pop()
        self.stk += valList[::-1]
        return self.hasNext()