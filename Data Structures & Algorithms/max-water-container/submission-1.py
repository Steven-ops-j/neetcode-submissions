class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0, len(heights) - 1
        best = 0
        while p1 < p2:
            best = max(best, min(heights[p2], heights[p1]) * (p2 - p1))
            if heights[p2] > heights[p1]:
                p1 += 1
            else:
                p2 -= 1
        return best
                
