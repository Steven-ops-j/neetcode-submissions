class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        def dfs(i):
            if i >= len(s):
                return 1
            if dp[i] != -1:
                return dp[i]
            if s[i] == '0':
                return 0
            dp[i] = dfs(i + 1)
            if i < len(s) - 1 and int(s[i:i+2]) < 27:
                dp[i] += dfs(i + 2)
            return dp[i]
        return dfs(0)