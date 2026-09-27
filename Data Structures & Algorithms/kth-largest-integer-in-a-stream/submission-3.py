import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = [x for x in nums]
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
