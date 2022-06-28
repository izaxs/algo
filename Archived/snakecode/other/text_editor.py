from collections import OrderedDict
from typing import Optional, Any

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
        if self.lo == len(self.content):
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

class Document2:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.content: str = ''
        self.lo: int = 0
        self.hi: int = 0
        self.history: list[tuple[str, int, int]] = []
        self.undoHistory: list[tuple[str, int, int]] = []

    def select(self, lo: int, hi: int) -> str:
        if lo < 0: lo = 0
        if hi > len(self.content): hi = len(self.content)
        if lo > hi: hi = lo
        self.lo, self.hi = lo, hi
        return self.content

    def append(self, text: str) -> str:
        if not text and self.lo == self.hi:
            return self.content
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

    def delete(self) -> str:
        if self.lo == len(self.content):
            return self.content
        if self.lo == self.hi:
            self.hi += 1
        return self.append('')

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

class Editor2:
    def __init__(self) -> None:
        self.defaultName = '####'
        self.clipboard = ''
        self.doc = Document2(self.defaultName)
        self.files: dict[str, Document2] = {}
        self.files[self.defaultName] = self.doc

    def create(self, name: str) -> Optional[str]:
        if name in self.files: return None
        self.files[name] = Document2(name)
        return self.doc.content

    def switch(self, name: str) -> Optional[str]:
        if name not in self.files: return None
        self.doc = self.files[name]
        return self.doc.content

    def select(self, lo: int, hi: int) -> str:
        return self.doc.select(lo, hi)

    def move(self, position: int) -> str:
        return self.doc.move(position)

    def append(self, text: str) -> str:
        return self.doc.append(text)

    def cut(self) -> str:
        doc = self.doc
        if doc.lo >= doc.hi: return doc.content
        self.clipboard = doc.content[doc.lo:doc.hi]
        doc.delete()
        return doc.content

    def paste(self) -> str:
        if not self.clipboard: return self.doc.content
        return self.doc.append(self.clipboard)

    def delete(self) -> str:
        return self.doc.delete()

    def undo(self) -> str:
        return self.doc.undo()

    def redo(self) -> str:
        return self.doc.redo()

def textEditor2_2(queries: list[Any]) -> list[Optional[str]]:
    e = Editor2()
    result: list[Optional[str]] = []
    for q in queries:
        if q[0] == 'APPEND':
            result.append(e.append(q[1]))
        elif q[0] == 'MOVE':
            result.append(e.move(int(q[1])))
        elif q[0] == 'DELETE':
            result.append(e.delete())
        elif q[0] == 'SELECT':
            result.append(e.select(int(q[1]), int(q[2])))
        elif q[0] == 'CUT':
            result.append(e.cut())
        elif q[0] == 'PASTE':
            result.append(e.paste())
        elif q[0] == 'UNDO':
            result.append(e.undo())
        elif q[0] == 'REDO':
            result.append(e.redo())
        elif q[0] == 'CREATE':
            result.append(e.create(q[1]))
        elif q[0] == 'SWITCH':
            result.append(e.switch(q[1]))
        else:
            raise ValueError(f'Unknown action: {q[0]}')
    return result
