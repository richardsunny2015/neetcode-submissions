class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = 0
        while r < len(nums):
            while r < len(nums) and nums[r] == val:
                r += 1
            if r >= len(nums):
                break
            original_r = nums[r]
            original_l = nums[l]
            nums[l] = original_r
            nums[r] = original_l
            l += 1
            r += 1
        for i, n in enumerate(nums):
            if n == val:
                return i
        return len(nums)