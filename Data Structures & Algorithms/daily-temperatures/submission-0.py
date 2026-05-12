class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i, temp in enumerate(temperatures):
            days = 0
            for j in range(i+1, len(temperatures)):
                if (temperatures[j] > temp):
                    days = j - i
                    break
            res.append(days)
        return res
