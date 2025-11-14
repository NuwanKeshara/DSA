class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        profit = 0
        min = prices[0]

        for i in prices:
            if min > i:
                min = i
            
            profit = max(profit, i - min)
        
        return profit