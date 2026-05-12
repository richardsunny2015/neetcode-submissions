class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                count = 0
                while i < len(nums) and nums[i] == 1:
                    count += 1
                    i += 1
                max_count = max(max_count, count)
            else:
                i += 1
                
        return max_count    