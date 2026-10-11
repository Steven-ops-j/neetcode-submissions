class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def dfs(ind):
            if ind >= len(nums):
                return 0
            if dp[ind] > -1:
                return dp[ind]
            dp[ind] = max(nums[ind] + dfs(ind + 2), dfs(ind + 1))
            return dp[ind]
        return dfs(0)