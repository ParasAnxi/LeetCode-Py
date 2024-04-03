class Solution:
    def solve(self, grid, n, m, i, j, dp):
      if i == n - 1 and j == m - 1:
        return grid[i][j]
      if dp[i][j] != -1:
        return dp[i][j]
      down = float('inf')
      right = float('inf')
      if i + 1 < n:
        down = grid[i][j] + self.solve(grid, n, m, i+1, j, dp)
      if j + 1 < m:
        right = grid[i][j] + self.solve(grid, n, m, i, j+1, dp)
      dp[i][j] = min(down, right)
      return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
      n = len(grid)
      m = len(grid[0])
      dp = [[-1] * m for _ in range(n)]
      return self.solve(grid, n, m, 0, 0, dp)

 def tab(self,grid):
      n = len(grid)
      m = len(grid[0])
      dp = [[0] * m for _ in range(n)]
      for i in range(n - 1, -1,-1):
        for j in range(m - 1,-1,-1):
          if i == n-1 and j == m - 1:
            dp[i][j] = grid[i][j]
          else:
            down = dp[i+1][j] if i + 1 < n else float('inf')
            right = dp[i][j+1] if j + 1 < m else float('inf')
            dp[i][j] = grid[i][j] + min(down,right)
      return dp[0][0]

    def minPathSum(self, grid: List[List[int]]) -> int:
      return self.tab(grid)

def so(self, grid):
      n = len(grid)
      m = len(grid[0])
      dp = [float('inf')] * m
      for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
          if i == n - 1 and j == m - 1:
            dp[j] = grid[i][j]
          else:
            down = dp[j] if i + 1 < n else float('inf')
            right = dp[j + 1] if j + 1 < m else float('inf')
            dp[j] = grid[i][j] + min(down, right)
      return dp[0]

    def minPathSum(self, grid: List[List[int]]) -> int:
      return self.so(grid)
        
        