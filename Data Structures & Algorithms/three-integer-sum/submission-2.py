class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mp = {}
        for i, value in enumerate(nums):
            if value not in mp:
                mp[value] = []
            mp[value].append(i)
        exists = set() 
        output = [] 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                need = -(nums[i] + nums[j])
                if need in mp:
                    for ind in mp[need]:
                        if ind != i and ind != j:
                            x = tuple(sorted([nums[i], nums[j], nums[ind]]))
                            if x not in exists:
                                exists.add(x)
                                output.append([nums[i], nums[j], nums[ind]]) 
                            break
        return output