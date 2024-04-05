class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(len(prices)):
          diff = prices[i] - mini
          profit = max(profit,diff)
          mini = min(mini,prices[i])
        return profit