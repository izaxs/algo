class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap: dict[str, str] = {}
        tMap: dict[str, str] = {}
        for cs, ct in zip(s, t):
            if ct != sMap.setdefault(cs, ct):
                return False
            if cs != tMap.setdefault(ct, cs):
                return False
        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
