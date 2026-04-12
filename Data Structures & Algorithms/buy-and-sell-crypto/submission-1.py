class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ctr = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                ctr = max(ctr, prices[j] - prices[i])
        return ctr