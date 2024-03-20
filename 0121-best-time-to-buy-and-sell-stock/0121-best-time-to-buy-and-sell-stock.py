class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i]-min_price)
            min_price = min(prices[i],min_price)
        return max_profit