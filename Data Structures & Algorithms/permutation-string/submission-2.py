from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = Counter(s1)
        elems = set(s1)
        l = 0
        for r in range(len(s2)):
            if s2[r] in need:
                need[s2[r]] -= 1
            if all(v <= 0 for v in need.values()):
                return True
            if r - l + 1 == len(s1):
                if s2[l] in elems:
                    need[s2[l]] = need.get(s2[l], 0) + 1
                l += 1
        if not need:
            return True
        return False

            