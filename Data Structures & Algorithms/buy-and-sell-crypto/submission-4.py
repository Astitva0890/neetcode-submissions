class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i ,j = 0 ,1
        mp = 0
        for j in range(len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                mp = max(mp , profit)
            else:
                i = j
        return mp


        