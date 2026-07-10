class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    # By Anshuman Pattanayak
        maxProfit = 0
        minPrice = prices[0]

        for p in prices :
            maxProfit = max(maxProfit ,(p - minPrice))
            minPrice = min(minPrice , p)
        
        return maxProfit
        