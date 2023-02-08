# Bulls and Cows

# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

# Constraints:

# 1 <= secret.length, guess.length <= 1000
# secret.length == guess.length
# secret and guess consist of digits only.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        freqs, bulls, cows = [0]*10, 0, 0
        for i, ch in enumerate(guess):
            if secret[i] == ch: bulls += 1
            else: freqs[ord(secret[i])-ord('0')] += 1
        for i, ch in enumerate(guess):
            if secret[i] != ch and freqs[o := ord(ch)-ord('0')] > 0:
                cows, freqs[o] = cows+1, freqs[o]-1
        return f'{bulls}A{cows}B'

if __name__ == '__main__':
    Solution().getHint("1123", "0111")
