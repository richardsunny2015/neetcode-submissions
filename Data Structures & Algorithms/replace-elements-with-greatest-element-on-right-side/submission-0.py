class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_nums = [-1] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            if i + 1 < len(arr):
                max_num = max(arr[i + 1], greatest_nums[i + 1])
                greatest_nums[i] = max_num
        return greatest_nums
