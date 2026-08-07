class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minLeft = [sys.maxsize] * len(prices)
        maxRight = [-sys.maxsize - 1] * len(prices)
        maxDiff = 0

        for i, price in enumerate(prices):
            if i == 0:
                minLeft[i] = price
                continue

            currMin = minLeft[i - 1]
            if currMin > price:
                minLeft[i] = price
            else:
                minLeft[i] = currMin
        
        for i, price in reversed(list(enumerate(prices))):
            if i == len(prices) - 1:
                maxRight[i] = price
                continue

            currMax = maxRight[i + 1]
            if currMax < price:
                maxRight[i] = price
            else:
                maxRight[i] = currMax
        
        for i in range(len(prices)):
            left = minLeft[i]
            right = maxRight[i]

            diff = right - left
            if diff > maxDiff:
                maxDiff = diff
        
        return maxDiff

        
