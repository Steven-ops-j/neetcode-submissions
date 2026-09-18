class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False;
        ds, dt = {}, {}
        for i in range(len(s)):
            if not ds.get(s[i]):
                ds[s[i]] = 0;
            if not dt.get(t[i]):
                dt[t[i]] = 0;
            dt[t[i]] += 1
            ds[s[i]] += 1
        print(dt, ds)
        return dt == ds