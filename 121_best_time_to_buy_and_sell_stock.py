class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        buy_price = prices[0]
        profit = 0

        for day in range(len(prices)):
            if prices[day] < buy_price:
                buy_price = prices[day]
            elif prices[day] - buy_price > profit:
                profit = prices[day] - buy_price

        return profit





# ======================================
solution = Solution()
prices = [7,1,5,3,6,4]
print solution.maxProfit(prices)
