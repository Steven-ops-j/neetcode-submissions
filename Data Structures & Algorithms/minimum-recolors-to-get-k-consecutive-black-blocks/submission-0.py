class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float("inf")
        numW = 0
        for l in blocks:
            if l == 'W':
                numW += 1
        for i in range(len(blocks) - k):
            op = 0
            for j in range(i, i + k):
                if blocks[j] == 'W':
                    op += 1
            ans = min(op, ans)
        if ans > 100:
            return numW
        return ans