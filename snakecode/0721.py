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

if __name__ == '__main__':
    s = Solution()
    inputs = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
    outputs = s.accountsMerge(inputs)
    print(outputs)