class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: list[Employee], id: int) -> int:
        empMap: dict[int, Employee] = {}
        for e in employees: empMap[e.id] = e

        def search(id: int) -> int:
            res = empMap[id].importance
            for subId in empMap[id].subordinates:
                res += search(subId)
            return res

        return search(id)
