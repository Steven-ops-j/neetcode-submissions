import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap) 
        while len(heap) > 1:
            biggest = -heapq.heappop(heap)
            heapq.heapify(heap)
            sec_biggest = -heapq.heappop(heap)
            if biggest != sec_biggest:
                heapq.heappush(heap, -(biggest - sec_biggest))
        return -heap[0] if heap else 0