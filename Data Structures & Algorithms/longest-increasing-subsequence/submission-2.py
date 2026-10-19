class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1] * 2001 for x in nums]

        def dfs(i, greatest):
            if i >= len(nums):
                return 0
            if dp[i][greatest + 1000] > -1:
                return dp[i][greatest + 1000]
            val = 0
            if nums[i] > greatest:
                val = dfs(i + 1, nums[i]) + 1
            val = max(val, dfs(i + 1, greatest))
            dp[i][greatest + 1000] = val
            return val
        return dfs(0, -1001)