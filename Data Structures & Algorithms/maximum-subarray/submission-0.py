class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = [0 for x in range(len(nums) + 1)]
        for i in range(len(nums)):
            pre[i + 1] = pre[i] + nums[i]
        ans = nums[0]
        low = 0
        for i in range(1, len(pre)):
            ans = max(ans, pre[i] - low)
            low = min(low, pre[i])
        return ans
