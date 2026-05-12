# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        m = len(pairs) // 2
        left = self.mergeSort(pairs[0:m])
        right = self.mergeSort(pairs[m:])
        return self.merge(left, right)
    def merge(self, left: List[Pair], right: List[Pair]) -> List[Pair]:
        left_pointer = 0
        right_pointer = 0
        result = []
        while left_pointer < len(left) and right_pointer < len(right):
            left_element = left[left_pointer]
            right_element = right[right_pointer]
            if left_element.key <= right_element.key:
                result.append(left_element)
                left_pointer += 1
            else:
                result.append(right_element)
                right_pointer += 1
        if left_pointer < len(left):
            for i in range(left_pointer, len(left)):
                result.append(left[i])
        if right_pointer < len(right):
            for i in range(right_pointer, len(right)):
                result.append(right[i])
        return result
