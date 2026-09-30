class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def permuter(nums, cur):
            if not len(nums):
                output.append(cur)
                return
            for i in range(len(nums)):
                permuter(nums[:i] + nums[i+1:], cur + [nums[i]])
        permuter(nums, [])
        return output
        