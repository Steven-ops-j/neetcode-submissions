import heapq, string
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-tasks.count(letter), letter) for letter in string.ascii_uppercase if tasks.count(letter)]
        heapq.heapify(heap)
        ans = 0
        while len(heap):
            cnt = 0
            stack = []
            while cnt <= n and len(heap):
                cnt += 1
                val, letter = heapq.heappop(heap)
                stack.append((-(-val - 1), letter))
                ans += 1
            for tup in stack:
                if -tup[0] > 0:
                    heapq.heappush(heap, tup)
            if len(heap) and stack[0] == heap[0]:
                ans += n + 1 - cnt
        return ans