class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[-1]:
                r = mid
            else:
                l = mid + 1
        shift = l
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[(mid + shift) % len(nums)] < target:
                l = mid + 1
            elif nums[(mid + shift) % len(nums)] > target:
                r = mid - 1
            else:
                return (mid + shift) % len(nums)
        return -1 