import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_to_point = defaultdict(list)
        distance = []
        for x, y in points:
            distance_to_point[-(x**2 + y**2)].append([x, y])
            distance.append(-(x**2 + y**2))
        heapq.heapify(distance)
        while len(distance) > k:
            heapq.heappop(distance)
            heapq.heapify(distance) 
        output = []
        for dis in distance:
            output.append(distance_to_point[dis].pop())
        return output