class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def permute(nums, cur, total):
            if total > target:
                return None
            if total == target:
                output.append(cur)
                return None
            for i in range(len(nums)):
                permute(nums[i:], cur + [nums[i]], total + nums[i])
                # if i < len(nums) - 1:
                #     permute(nums[i+1:], cur + [nums[i]] + [nums[i + 1]], total + nums[i] + nums[i + 1])
        permute(nums, [], 0)
        return output 
