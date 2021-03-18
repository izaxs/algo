class MinHeap:

    def __init__(self):
        self.size = 0
        self.data = []
    
    def parent(self, i: int) -> int:
        return (i-1)//2 if i >= 0 else 0
    
    def left(self, i: int) -> int:
        return i*2+1 if i >= 0 else 0
    
    def right(self, i: int) -> int:
        return i*2+2 if i >= 0 else 0

    def swap(self, i: int, j: int):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def up(self, i: int):
        if i <= 0: return
        p = self.parent(i)
        if self.data[i] < self.data[p]:
            self.swap(i, p)
            self.up(p)
        
    def down(self, i: int):
        if i >= self.size: return
        right = self.right(i)
        if right < self.size and self.data[i] > self.data[right]:
            self.swap(i, right)
            self.down(right)
            return
        left = self.left(i)
        if left < self.size and self.data[i] > self.data[left]:
            self.swap(i, left)
            self.down(left)

    def push(self, item: int):
        i = self.size
        self.data.append(item)
        self.size += 1
        self.up(i)

    def pop(self) -> int:
        if self.size <= 0: raise IndexError("Empty heap")
        root = self.data[0]
        self.size -= 1
        self.data[0] = self.data[self.size]
        self.down(0)
        return root

    def peek(self) -> int:
        if self.size <= 0: raise IndexError("Empty heap")
        return self.data[0]
