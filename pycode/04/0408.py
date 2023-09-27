# Valid Word Abbreviation

# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

#     "s10n" ("s ubstitutio n")
#     "sub4u4" ("sub stit u tion")
#     "12" ("substitution")
#     "su3i1u2on" ("su bst i t u ti on")
#     "substitution" (no substrings replaced)

# The following are not valid abbreviations:

#     "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
#     "s010n" (has leading zeros)
#     "s0ubstitution" (replaces an empty substring)

# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n, iWord = 0, 0
        for c in abbr:
            if c.isalpha():
                if n:
                    iWord += n
                    n = 0
                if iWord >= len(word) or word[iWord] != c: return False
                iWord = iWord + 1 if not n else iWord
            else:
                if not n and c == '0': return False
                n = n * 10 + int(c)
        return iWord + n == len(word)
    
    def validWordAbbreviation2(self, word: str, abbr: str) -> bool:
        skip, iWord = 0, -1
        for c in abbr:
            if c.isalpha():
                iWord, skip = iWord + skip + 1, 0
                if iWord >= len(word) or word[iWord] != c: return False
            else:
                if skip == 0 and c == '0': return False
                skip = skip * 10 + int(c)
        return iWord + skip == len(word) - 1
    
    def validWordAbbreviation3(self, word: str, abbr: str) -> bool:
        number, wordIndex = 0, 0
        for c in abbr:
            if c.isalpha():
                wordIndex += number
                number = 0
                if wordIndex >= len(word) or word[wordIndex] != c:
                    return False
                wordIndex += 1
            else:
                curNum = int(c)
                if not curNum and not number: return False
                number = number * 10 + curNum
        return wordIndex + number == len(word)
    
if __name__ == '__main__':
    r = Solution().validWordAbbreviation2("internationalization", "i18n")
    assert r
                