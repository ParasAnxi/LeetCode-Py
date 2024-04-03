class Solution:
    def solve(self, m, n, i, j, dp):
      if i == m - 1 and j == n - 1:
        return 1
      if dp[i][j] != -1:
        return dp[i][j]
      down, right = 0, 0
      if i + 1 < m:
        down = self.solve(m, n, i+1, j, dp)
      if j + 1 < n:
        right = self.solve(m, n, i, j+1, dp)
      dp[i][j] = down + right
      return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        return self.solve(m, n,0,0,dp)
    
# tabulation
def tab(self,m,n):
      dp = [[0] * n for _ in range(m)]
      dp[m - 1][n - 1] = 1
      for i in range(m - 1, - 1, -1):
        for j in range(n - 1, -1, - 1):
          if i == m - 1 and j == n - 1:
            continue
          down = dp[i + 1][j] if i + 1 < m else 0
          right = dp[i][j + 1] if j + 1 < n else 0
          dp[i][j] = down + right

      return dp[0][0]
    def uniquePaths(self, m: int, n: int) -> int:
        return self.tab(m,n)