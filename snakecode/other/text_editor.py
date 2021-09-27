from collections import OrderedDict
from typing import Optional

shouldPrint = True

class Document:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.content: str = ""
        self.lo: int = 0
        self.hi: int = 0
        self.history: list[tuple[str, int, int]] = []
        self.undoHistory: list[tuple[str, int, int]] = []

    def select(self, lo: int, hi: int) -> str:
        if lo < 0: lo = 0
        if hi > len(self.content): hi = len(self.content)
        if hi < lo: hi = lo
        self.lo = lo
        self.hi = hi
        return self.content[lo:hi]

    def append(self, text: str) -> str:
        if not text and self.lo == self.hi: return self.content
        self.history.append((self.content, self.lo, self.hi))
        self.undoHistory.clear()
        pre = self.content[:self.lo]
        after = self.content[self.hi:]
        self.content = pre+text+after
        self.lo = self.lo+len(text)
        self.hi = self.lo
        return self.content

    def move(self, position: int) -> str:
        if position > len(self.content):
            position = len(self.content)
        elif position < 0:
            position = 0
        self.lo = position
        self.hi = position
        return self.content

    def undo(self) -> str:
        if not self.history: return self.content
        self.undoHistory.append((self.content, self.lo, self.hi))
        self.content, self.lo, self.hi = self.history.pop()
        return self.content

    def redo(self) -> str:
        if not self.undoHistory: return self.content
        self.history.append((self.content, self.lo, self.hi))
        self.content, self.lo, self.hi = self.undoHistory.pop()
        return self.content

    def delete(self) -> str:
        if self.hi == len(self.content):
            return self.content
        if self.lo == self.hi:
            self.hi += 1
        return self.append('')

    def close(self) -> None:
        self.clipboard = ''
        self.history.clear()
        self.undoHistory.clear()
        self.lo = len(self.content)
        self.hi = self.lo

class Editor:
    def __init__(self) -> None:
        self.clipboard = ''
        self.closed: dict[str, Document] = {}
        self.opened: OrderedDict[str, Document] = OrderedDict() # the end one is active

    def doc(self) -> Document:
        if not self.opened: raise Exception()
        name, doc = self.opened.popitem()
        self.opened[name] = doc
        self.opened.move_to_end(name)
        return doc

    def open(self, name: str) -> str:
        if name in self.opened:
            doc = self.opened[name]
        elif name in self.closed:
            doc = self.closed.pop(name)
            self.opened[name] = doc
        else:
            doc = Document(name)
            self.opened[name] = doc
        self.opened.move_to_end(name)
        return doc.content

    def close(self, name: Optional[str] = None) -> None:
        if not self.opened or (name and name not in self.opened): raise Exception()
        if not name:
            name, doc = self.opened.popitem()
        else:
            doc = self.opened.pop(name)
        doc.close()
        self.closed[name] = doc

    def select(self, lo: int, hi: int) -> str:
        return self.doc().select(lo, hi)

    def append(self, text: str) -> str:
        return self.doc().append(text)

    def move(self, position: int) -> str:
        return self.doc().move(position)

    def copy(self) -> str:
        doc = self.doc()
        self.clipboard = doc.content[doc.lo:doc.hi]
        return self.clipboard

    def paste(self) -> str:
        return self.doc().append(self.clipboard)

    def undo(self) -> str:
        return self.doc().undo()

    def redo(self) -> str:
        return self.doc().redo()

    def delete(self) -> str:
        return self.doc().delete()

def test1():
    e = Editor()
    print(e.open('t1.txt'))
    print(e.append('hello! world!'))
    print(e.move(5))
    print(e.delete())
    print(e.append(','))

def test2():
    e = Editor()
    print(e.open('t2.txt'))
    print(e.append('hello, world!'))
    print(e.select(5, 12))
    print(e.copy())
    print(e.move(12))
    print(e.paste())
    print(e.paste())

def test3():
    e = Editor()
    print(e.open('t3.txt'))
    print(e.append('hello, world!'))
    print(e.select(7, 12))
    print(e.delete())
    print(e.move(6))
    print(e.undo())
    print(e.undo())
    print(e.redo())
    print(e.redo())

def test4():
    e = Editor()
    print(e.open('t4-1.txt'))
    print(e.append('hello, world!'))
    print(e.select(7, 12))
    print(e.copy())
    print(e.delete())
    print(e.open('t4-2.txt'))
    print(e.paste())
    print(e.close('t4-2.txt'))
    print(e.undo())
    print(e.open('t4-2.txt'))
    print(e.undo())

if __name__ == '__main__':
    test4()