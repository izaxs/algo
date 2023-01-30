# Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:        
    def reverseWords(self, s: str) -> str:
        strArr = [*s]
        def reverse(lo: int, hi: int):
            while lo < hi:
                strArr[lo], strArr[hi] = strArr[hi], strArr[lo]
                lo, hi = lo+1, hi-1
        cur = 0
        while cur < len(s):
            while cur < len(s) and strArr[cur] == ' ':
                cur += 1
            curEnd = cur+1
            while curEnd < len(s) and strArr[curEnd] != ' ':
                curEnd += 1
            reverse(cur, curEnd-1)
            cur = curEnd+1
        return ''.join(strArr)

if __name__ == '__main__':
    print(Solution().reverseWords('Good Ding'))