# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        eGroup: dict[str, str] = {} # email -> email
        enames: dict[str, set[str]] = {} # name -> set(email)

        def getRoot(key: str) -> str:
            if key in eGroup:
                while eGroup[key] != key: key = eGroup[key]
            return key

        # build unions graph
        for acc in accounts:
            name = acc[0]
            root = getRoot(acc[1]) # use the first element's group as root group
            for email in acc[1:]:
                emails = enames.setdefault(name, set())
                emails.add(email)
                preRoot = getRoot(email)
                eGroup[preRoot] = root

        res: list[list[str]] = []
        for name, emails in enames.items():
            # extract group from union graph
            rootGroups: dict[str, set[str]] = {} # rootEmail -> emails
            for email in emails:
                root = getRoot(email)
                group = rootGroups.setdefault(root, set())
                group.add(email)
            for root, group in rootGroups.items():
                personData: list[str] = []
                for email in group: personData.append(email)
                personData.sort()
                personData = [name]+personData
                res.append(personData)
        return res

    class UF:
        def __init__(self, N: int) -> None:
            self.parent: list[int] = [i for i in range(N)]

        def find(self, child: int) -> int:
            while child != self.parent[child]: child = self.parent[child]
            return child

        def union(self, child: int, parent: int): # union i2 group into i1
            self.parent[self.find(child)] = self.find(parent)
            

    def accountsMerge2(self, accounts: list[list[str]]) -> list[list[str]]:
        emailToAccounts: dict[str, list[int]] = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                emailToAccounts.setdefault(email, []).append(i)
        uf = Solution.UF(len(accounts))
        for (parent, *children) in emailToAccounts.values():
            for child in children:
                uf.union(child, parent)
        mergedAccounts: dict[int, list[str]] = {}
        for email, (account, *_) in emailToAccounts.items():
            mergedAccounts.setdefault(uf.find(account), []).append(email)
        return [[accounts[account][0], *sorted(emails)] for (account, emails) in mergedAccounts.items()]

    def accountsMerge3(self, accounts: list[list[str]]) -> list[list[str]]:
        emailOwner: dict[str, int] = {}
        unionFinder = Solution.UF(len(accounts))
        for accountId, (_, *emails) in enumerate(accounts):
            for email in emails:
                ownerId = emailOwner.setdefault(email, accountId)
                unionFinder.union(accountId, ownerId)
        mergedAccounts: dict[int, list[str]] = {}
        for email, accountId in emailOwner.items():
            mergedAccounts.setdefault(unionFinder.find(accountId), []).append(email)
        return [[accounts[accountId][0], *sorted(emails)] for (accountId, emails) in mergedAccounts.items()]


        


if __name__ == '__main__':
    # s = Solution()
    # inputs = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
    # outputs = s.accountsMerge(inputs)
    # print(outputs)

    s = Solution()
    inputs = [
        ["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"],
    ]
    outputs = s.accountsMerge3(inputs)
