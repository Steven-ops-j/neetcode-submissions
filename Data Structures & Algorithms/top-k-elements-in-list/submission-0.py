class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for x in nums:
            if not dic.get(x):
                dic[x] = 0
            dic[x] += 1
        return [row[0] for row in sorted(dic.items(), key=lambda x: x[1], reverse=True)[:k]]