class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)-1
        profit = 0
        while n > 0:
            i = 0
            mn = 0
            while i < n:
                if prices[mn] > prices[i]:
                    mn = i
                i+=1
            if profit < (prices[n] - prices[mn]):
                profit = (prices[n] - prices[mn])
            n-=1  
        return max(profit, 0)