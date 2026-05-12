class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            midpoint = ((r - l) // 2) + l
            num = nums[midpoint]
            if num < target:
                l = midpoint + 1
            elif num > target:
                r = midpoint - 1
            else:
                return midpoint
        return -1