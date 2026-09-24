class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maxp = 0 
        for j in range(len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxp = max(maxp , profit)
            else :
                i = j
        return maxp
        