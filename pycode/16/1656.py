# 1656. Design an Ordered Stream

# There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.

# Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.

# Implement the OrderedStream class:

#     OrderedStream(int n) Constructs the stream to take n values.
#     String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.

# Constraints:

#     1 <= n <= 1000
#     1 <= id <= n
#     value.length == 5
#     value consists only of lowercase letters.
#     Each call to insert will have a unique id.
#     Exactly n calls will be made to insert.

class OrderedStream:

    def __init__(self, n: int):
        self.N = n
        self.next = 1
        self.map: dict[int, str] = {}

    def insert(self, idKey: int, value: str) -> list[str]:
        self.map[idKey] = value
        result = []
        while nextValue := self.map.pop(self.next, None): # value always has length 5
            result.append(nextValue)
            self.next += 1
        return result
    
class OrderedStream2:

    def __init__(self, n: int):
        self.store: list[str | None] = [None] * n
        self.next = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        self.store[idKey-1] = value
        result = []
        while self.next < len(self.store) and self.store[self.next]: # value always has length 5
            result.append(self.store[self.next])
            self.next += 1
        return result


# OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)