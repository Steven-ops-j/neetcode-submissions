class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, r = 0, 0
        ans = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            window_len = r - l + 1
            while window_len - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                window_len -= 1
            ans = max(ans, window_len)
            r += 1
        return ans

