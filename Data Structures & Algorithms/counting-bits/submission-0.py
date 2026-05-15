class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0] * (n + 1)
        for i in range(n + 1):
            m = i
            while m > 0:
                if m & 1 == 1:
                    counts[i] += 1
                m = m >> 1
        return counts