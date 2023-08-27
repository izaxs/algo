# Users can refer each other to Robinhood. We want keep track of who is responsible for the most referrals and display the top users on a leaderboard.

# If user A refers user B, and user B refers user C. Then the leaderboard looks like this:

# User A: 2 Referrals
# User B: 1 Referrals
# User C: 0 Referrals

# Explanation: User B has 1 referral for referring user C. User A has 2 referrals because they referred user B, and they also inherit the referral for user C since user B is one of their referrals.

# Given a list of referrals (Example Input: [ ["A","B"] , ["B", "C"] ], write a function that determines the leaderboard order.



class Solution:
    # Tree solution
    def getLeaderBoard(self, referrals: list[tuple[str, str]]) -> list[tuple[str, int]]:
        class UserNode:
            def __init__(self):
                self.referrals: list[UserNode] = []
                self.count = -1
        def traversal(user: UserNode) -> int:
            if user.count >= 0: return user.count
            user.count = 0
            for r in user.referrals:
                user.count += traversal(r) + 1
            return user.count
        
        users: dict[str, UserNode] = {}
        for referrer, referral in referrals:
            referrerNode = users.setdefault(referrer, UserNode())
            referralNode = users.setdefault(referral, UserNode())
            referrerNode.referrals.append(referralNode)

        result: list[tuple[str, int]] = []
        for name, node in users.items():
            result.append((name, traversal(node)))
        result.sort(key=lambda x: x[1], reverse=True)
        return result
    
    # Topological sort solution
    def getLeaderBoard2(self, referrals: list[tuple[str, str]]) -> list[tuple[str, int]]:
        from collections import deque, Counter

        referrerMap: dict[str, str] = {}
        degrees: dict[str, int] = {}
        for referrer, referral in referrals:
            referrerMap[referral] = referrer
            referrerDegree = degrees.get(referrer, 0)
            degrees[referrer] = referrerDegree + 1
            degrees.setdefault(referral, 0)

        nextLevel: deque[str] = deque()
        for user, dg in degrees.items():
            if not dg: nextLevel.append(user)
        
        counter: Counter[str] = Counter()
        while nextLevel:
            size = len(nextLevel)
            for _ in range(size):
                user = nextLevel.popleft()
                referrer = referrerMap.get(user)
                if referrer == None: continue
                counter[user] = counter[user]
                counter[referrer] += counter[user] + 1
                degrees[referrer] -= 1
                if not degrees[referrer]:
                    nextLevel.append(referrer)
        return counter.most_common()
                
        
        
            
if __name__ == '__main__':
    referrals = [("A", "B"), ("B", "C"), ("A", "D"), ("B", "E"), ("F", "G"), ("G", "Z")]
    referrals = [("A", "B"), ("C", "D")]
    result = Solution().getLeaderBoard2(referrals)
    print(result)
            