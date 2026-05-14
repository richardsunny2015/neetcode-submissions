class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        sums = [0] * 2
        for i in range(len(nums)):
            if i < 2:
                sums[i] = nums[i]
            else:
                tmp = sums[1]
                sums[1] = max(sums[1], sums[0] + nums[i])
                sums[0] = max(sums[0], tmp)
        return sums[1]