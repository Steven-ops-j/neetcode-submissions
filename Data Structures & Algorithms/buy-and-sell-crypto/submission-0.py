class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCoin = prices[0]    
        output = 0
        for price in prices:
            minCoin = min(minCoin, price)
            output = max(output, price - minCoin)
        return output