from dataclasses import dataclass

@dataclass
class Record:
    name: str
    phone: str


r = Record('John', '1234567890')
r2 = Record('John', '1234567890')
assert r == r2
