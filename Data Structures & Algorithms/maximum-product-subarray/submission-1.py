class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[-1]
        curmax = nums[-1]
        curmin = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            curmax *= nums[i]
            curmin *= nums[i]
            if curmax < curmin:
                curmax, curmin = curmin, curmax
            if curmax < nums[i]:
                curmax = nums[i]
            if curmin > nums[i]:
                curmin = nums[i]
            ans = max(ans, curmax)
        return ans
            