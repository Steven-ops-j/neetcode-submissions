class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 1_000_000_000
        best = r
        piles.sort()
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for pile in piles:
                total += (pile - 1) // mid + 1
            if total > h:
                l = mid + 1
            else:
                r = mid - 1
                best = mid
        return best 