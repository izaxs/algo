# 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period

# LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

# You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

# Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

# Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

# Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.

# Constraints:

#     1 <= keyName.length, keyTime.length <= 105
#     keyName.length == keyTime.length
#     keyTime[i] is in the format "HH:MM".
#     [keyName[i], keyTime[i]] is unique.
#     1 <= keyName[i].length <= 10
#     keyName[i] contains only lowercase English letters.

class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        def timeOrdinal(time: str) -> int:
            hourStr, minStr = time.split(':')
            return int(hourStr) *  60 + int(minStr)
        userAccess: dict[str, list[int]] = {}
        for i, time in enumerate(keyTime):
            userAccess.setdefault(keyName[i], []).append(timeOrdinal(time))
        usersWarned: list[str] = []
        for userName, accesses in userAccess.items():
            accesses.sort()
            for i in range(len(accesses)-2):
                if accesses[i] + 60 >= accesses[i+2]:
                    usersWarned.append(userName)
                    break
        return sorted(usersWarned)
                
