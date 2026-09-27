import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-x for x in nums]
        heapq.heapify(arr)
        while len(arr) > len(nums) - k + 1:
            heapq.heappop(arr)
        return -arr[0]