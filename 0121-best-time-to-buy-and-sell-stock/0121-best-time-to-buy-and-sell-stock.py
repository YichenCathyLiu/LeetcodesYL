class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]

        for j in range(len(prices)):
            max_profit = max(max_profit,prices[j]-min_price)
            min_price = min(min_price,prices[j])
        return max_profit
