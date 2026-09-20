class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers = sorted(numbers)
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                return [p1 + 1, p2 + 1]
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
                continue
            while p1 < p2 and numbers[p1] + numbers[p2] > target:
                p2 -= 1
            