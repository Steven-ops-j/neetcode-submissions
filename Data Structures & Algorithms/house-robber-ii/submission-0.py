class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first = [-1] * (len(nums) - 1)
        second = [-1] * (len(nums) - 1)
        
        def dfs(nums, i, dp):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(dfs(nums, i + 1, dp), dfs(nums, i + 2, dp) + nums[i])
            return dp[i]

        dfs(nums[:(len(nums) - 1)], 0, first)
        dfs(nums[1:], 0, second)
        return max(first[0], second[0]) 

            