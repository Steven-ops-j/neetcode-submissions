import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         product = math.prod([x if x != 0 else 1 for x in nums])
         exists0 = nums.count(0)
         if exists0 > 1:
            product = 0
         if exists0:
            return [int(product) if x == 0 else 0 for x in nums]
         return [int(product / x) for x in nums]
