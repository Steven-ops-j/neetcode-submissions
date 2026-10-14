class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        for i in range(len(s)):
            onew_l = i - 1
            onew_r = i + 1
            enew_l = i
            enew_r = i + 1
            while onew_l >= 0 and onew_r < len(s) and s[onew_l] == s[onew_r]:
                onew_l -= 1
                onew_r += 1
                ans += 1

            while enew_l >= 0 and enew_r < len(s) and s[enew_l] == s[enew_r]:
                enew_l -= 1
                enew_r += 1
                ans += 1
        return ans 