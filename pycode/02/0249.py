# 249. Group Shifted Strings

# We can shift a string by shifting each of its letters to its successive letter.

#     For example, "abc" can be shifted to be "bcd".

# We can keep shifting the string to form a sequence.

#     For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

# Constraints:

#     1 <= strings.length <= 200
#     1 <= strings[i].length <= 50
#     strings[i] consists of lowercase English letters.


class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        def shift(s: str) -> str:
            if not s: return s
            base = list(s)
            diff = ord(base[0]) - ord('a')
            for i, v in enumerate(base):
                newOrd = ord(v)-diff
                if newOrd < ord('a'): newOrd += 26
                base[i] = str(newOrd)
            return ''.join(base)
        
        seen: dict[str, list[str]] = {}
        for s in strings:
            seen.setdefault(shift(s), []).append(s)
        return [g for g in seen.values()]