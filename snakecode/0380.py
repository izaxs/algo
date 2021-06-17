class RandomizedSet:
    def __init__(self):
        self.lookup: dict[int, int] = {}
        self.nums: list[int] = []

    def insert(self, val: int) -> bool:
        addr = len(self.nums)
        realAddr = self.lookup.setdefault(val, addr)
        if realAddr != addr: return False
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        addr = self.lookup.pop(val, None)
        if addr is None: return False
        mover = self.nums.pop()
        if addr < len(self.nums):
            self.lookup[mover] = addr
            self.nums[addr] = mover
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.nums) if self.nums else 0

s = RandomizedSet()
s.insert(1)
s.insert(2)
s.remove(1)
print(s.insert(2))
