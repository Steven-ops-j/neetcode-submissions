class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other = {} 
        for i in range(len(nums)):
            other[nums[i]] = i;
        for i in range(len(nums)):
            if other.get(target - nums[i]) and other.get(target - nums[i]) != i:
                return [i, other[target-nums[i]]]
            
        
    