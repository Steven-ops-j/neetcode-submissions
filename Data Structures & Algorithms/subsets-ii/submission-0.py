class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        def permute(nums, cur):
            output.append(cur)
            if not len(nums):
                return
            i = 0
            while i < len(nums):
                permute(nums[i+1:], cur + [nums[i]])
                base = nums[i]
                while i < len(nums) and nums[i] == base:
                    i += 1
        permute(nums, [])
        return output
                