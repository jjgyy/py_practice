class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for day in range(len(prices)-1):
            differ = prices[day+1] - prices[day]
            if differ > 0:
                profit += differ
        return profit


# ===============================================
solution = Solution()
prices = [1,2,3,4,5]
print solution.maxProfit(prices)
