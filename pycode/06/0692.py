# Top K Frequent Words

# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# Constraints:

#     1 <= words.length <= 500
#     1 <= words[i].length <= 10
#     words[i] consists of lowercase English letters.
#     k is in the range [1, The number of unique words[i]]

# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
from heapq import nsmallest

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]: 
        counter: dict[str, int] = {}
        for w in words: counter[w] = counter.get(w, 0)+1
        hp = ((-count, word) for word, count in counter.items())
        targetWords = nsmallest(k, hp)
        return [word for _, word in targetWords]

    # Full sort is ironically faster
    def topKFrequent2(self, words: list[str], k: int) -> list[str]: 
        counter: dict[str, int] = {}
        for w in words: counter[w] = counter.get(w, 0)+1
        counterList = [(-count, word) for word, count in counter.items()]
        counterList.sort()
        return [word for _, word in counterList[:k]]