class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1] * len(s) for x in s]
        ans = (0, 0) 
        def dfs(i, j):
            nonlocal ans
            if dp[i][j] != -1:
                return dp[i][j]
            if i == j:
                dp[i][j] = 1
            elif j - i == 1:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dfs(i + 1, j - 1)
            if ans[1] - ans[0] < j - i and dp[i][j]:
                ans = (i, j)
            return dp[i][j] 

        for i in range(len(s)):
            for j in range(i, len(s)):
                dfs(i, j)
        return s[ans[0]:ans[1] + 1]