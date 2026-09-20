class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        went_thru = set()
        snums = set(nums)
        output = 0
        for x in nums:
            if x in went_thru:
               continue
            sequence = 0
            while x in snums:
                went_thru.add(x)
                x -= 1
                sequence += 1
            output = max(output, sequence)             
        return output