class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [-1] * (len(s) + 1)
        dp[-1] = 1
        def dfs(i):
            print(i, dp)
            if dp[i] > -1:
                return dp[i]
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    print(s[i:j+1])
                    val = 0
                    if dp[j + 1] > -1:
                        val = dp[j + 1]
                    else:
                        val = dfs(j + 1)
                    if val:
                        return 1
            dp[i] = 0
            return 0
        return bool(dfs(0))