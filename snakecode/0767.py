import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S or len(S) <= 1: return S
        freqs = Counter(S)
        pq = [(-count, char) for char, count in freqs.items()]
        heapq.heapify(pq)
        preCount, preChar, seq = 0, '', []
        while pq:
            count, char = heapq.heappop(pq)
            seq.append(char)
            if preCount < 0: heapq.heappush(pq, (preCount, preChar))
            preCount, preChar = count + 1, char
        if preCount < 0: return ''
        return ''.join(seq)