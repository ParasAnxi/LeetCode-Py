class Solution:
    def mem(self, prices, index, buy, limit, dp):
      n = len(prices)
      if index == n or limit == 0:
        return 0
      if dp[index][buy][limit] != -1:
        return dp[index][buy][limit]

      profit = 0
      if buy:
        profit = max(-prices[index] + self.mem(prices, index + 1,
                     0, limit, dp), self.mem(prices, index + 1, 1, limit, dp))
      else:
        profit = max(prices[index] + self.mem(prices, index + 1, 1,
                     limit - 1, dp), self.mem(prices, index + 1, 0, limit, dp))

      dp[index][buy][limit] = profit
      return profit

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[-1 for _ in range(2 + 1)] for _ in range(2)]
              for _ in range(len(prices))]
        return self.mem(prices, 0, 1, 2, dp)


def maxProfit(self, prices: List[int]) -> int:
    x = float('inf')
    y = float('inf')
    z = 0
    w = 0
    for price in prices:
        x = min(x, price)
        z = max(z, price - x)
        y = min(y, price - z)
        w = max(w, price - y)
    return w
