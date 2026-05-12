class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i == 0 or nums[i] > nums[i - 1]:
                i += 1
            else:
                nums.pop(i)
        return len(nums)
            