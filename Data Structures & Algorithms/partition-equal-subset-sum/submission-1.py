class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        def dfs(i, cur):
            if i >= len(nums):
                return False
            if total - cur == cur:
                return True
            return dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)
        return dfs(0, 0) 