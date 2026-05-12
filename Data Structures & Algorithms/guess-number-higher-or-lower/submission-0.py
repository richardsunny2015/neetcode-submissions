# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.guess(1, n)
    def guess(self, s, e):
        # should never happen I think
        if s > e:
            return -1
        mid = (s + e) // 2
        result = guess(mid)
        if result < 0:
            return self.guess(s, mid - 1)
        if result > 0:
            return self.guess(mid + 1, e)
        return mid