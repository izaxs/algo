from dataclasses import dataclass
from typing import Generic, TypeVar, TypeVarTuple
from uuid import UUID

TKey = TypeVar('TKey', UUID, int, str)
TVal = TypeVar('TVal')
TValues = TypeVarTuple('TValues')

@dataclass
class DataClassRecord(Generic[TKey, TVal]):
    key: TKey
    value: TVal

class Record(Generic[TKey, *TValues]):
    key: TKey
    values: tuple[*TValues]

    def __init__(self, key: TKey, *values: *TValues):
        self.key = key
        self.values = values


r = DataClassRecord('a', 1)
r2 = DataClassRecord('b', 2)
assert r == r2
