class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        def dfs(total):
            if total < 0:
                return -100000
            if dp[total] < float("inf"):
                return dp[total]
            least = -1
            for i in range(len(coins)):
                val = dfs(total - coins[i])
                if val > -1:
                    least = min(least, val + 1)
                    if least == -1:
                        least = val + 1
            dp[total] = least
            return dp[total]
        return dfs(amount)