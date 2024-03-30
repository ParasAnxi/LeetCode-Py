class Solution:
    def solve(self, s: str, p: str, n: int, m: int, i: int, j: int, dp: List[List[int]]) -> bool:
      if i >= n and j >= m:
        return True
      if dp[i][j] != -1:
        return dp[i][j]

      match = (i < n) and (j < m) and (s[i] == p[j] or p[j] == '.')

      if j + 1 < m and p[j + 1] == '*':
        dp[i][j] = self.solve(
            s, p, n, m, i, j+2, dp) or (match and self.solve(s, p, n, m, i + 1, j, dp))
      else:
        dp[i][j] = match and self.solve(s, p, n, m, i + 1, j + 1, dp)

      return dp[i][j]

    def isMatch(self, s: str, p: str) -> bool:
      n = len(s)
      m = len(p)
      dp = [[-1] * (m + 1) for _ in range(n + 1)]
      return self.solve(s, p, n, m, 0, 0, dp)
