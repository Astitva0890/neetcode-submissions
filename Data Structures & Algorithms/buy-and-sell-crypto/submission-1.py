class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(i + 1 , len(prices)):
                buy = prices[i]
                sell = prices[j]
                res =max(res,sell-buy)
        return res
        