class Solution:
    def mem(self, prices, k, index, operation, dp):
      if index == len(prices):
        return 0
      if operation == 2 * k:
        return 0
      if dp[index][operation] != -1:
        return dp[index][operation]

      profit = 0
      if operation & 1:
         profit = max(prices[index] + self.mem(prices, k, index + 1, operation + 1, dp),
                      self.mem(prices, k, index + 1, operation, dp))
      else:
        profit = max(-prices[index] + self.mem(prices, k, index + 1, operation + 1, dp),
                     self.mem(prices, k, index + 1, operation, dp))

      dp[index][operation] = profit
      return profit

    def maxProfit(self, k: int, prices: List[int]) -> int:
       dp = [[-1] * (2*k) for _ in range(len(prices))]
       return self.mem(prices, k,0,0,dp)