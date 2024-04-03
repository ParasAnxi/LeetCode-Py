# memoization
class Solution:
    def solve(self, grid, n, m, i, j, dp):
      if i == n - 1 and j == m - 1 and grid[i][j] == 0:
        return 1
      if i >= n or j >= m or grid[i][j] == 1:
        return 0
      if dp[i][j] != -1:
        return dp[i][j]
      down = self.solve(grid, n, m, i+1, j, dp)
      right = self.solve(grid, n, m, i, j+1, dp)
      dp[i][j] = down + right
      return dp[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1] * m for _ in range(n)]
        return self.solve(obstacleGrid, n,m,0,0,dp)

# tabulation
def tab(self,grid):
      n = len(grid)
      m = len(grid[0])
      dp = [[0] * m for _ in range(n)]
      for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
          if i == n - 1 and j == m - 1 and grid[i][j] == 0:
            dp[i][j] = 1
          elif i < n and j < m and grid[i][j] == 0:
            down = dp[i + 1][j] if i + 1 < n else 0
            right = dp[i][j + 1] if j + 1 < m else 0
            dp[i][j] = down + right
      return dp[0][0]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.tab(obstacleGrid)

# space optimization
def so(self,grid):
      n = len(grid)
      m = len(grid[0])
      dp = [0] * m
      for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1,-1):
          if grid[i][j] == 1:
            dp[j] = 0 
            continue
          if i == n - 1 and j == m - 1 and grid[i][j] == 0:
            dp[j] = 1
          elif i < n and j < m and grid[i][j] == 0:
            down = dp[j] if i + 1 < n else 0
            right = dp[j + 1] if j + 1 < m else 0 
            dp[j] = down + right
      return dp[0]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.so(obstacleGrid)