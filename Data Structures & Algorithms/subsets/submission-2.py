class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        def permute(nums, cur):
            if not nums:
                return None
            for i in range(len(nums)):
                new_arr = cur + [nums[i]]
                output.append(new_arr)
                ret = permute(nums[i+1:], new_arr) 
                if ret:
                    output.append(ret)
        permute(nums, [])
        return output