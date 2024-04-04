class Solution:
    def mem(self, a: str, b: str, i: int, j: int, dp: List[List[int]]) -> int:
      if i == len(a):
          return len(b) - j
      if j == len(b):
          return len(a) - i
      if dp[i][j] != -1:
          return dp[i][j]
      ans = 0

      if a[i] == b[j]:
          ans = self.mem(a, b, i + 1, j + 1, dp)
      else:
          insert = 1 + self.mem(a, b, i, j + 1, dp)
          replace = 1 + self.mem(a, b, i + 1, j + 1, dp)
          delete = 1 + self.mem(a, b, i + 1, j, dp)
          ans = min(insert, replace, delete)
      dp[i][j] = ans
      return ans

    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        return self.mem(word1, word2,0,0,dp)
    
def tab(self, a: str, b: str) -> int:
      dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

      for j in range(len(b)):
        dp[len(a)][j] = len(b) - j

      for i in range(len(a)):
        dp[i][len(b)] = len(a) - i

      for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
          if a[i] == b[j]:
            dp[i][j] = dp[i + 1][j + 1]
          else:
            insert = 1 + dp[i][j + 1]
            replace = 1 + dp[i + 1][j + 1]
            delete = 1 + dp[i + 1][j]
            dp[i][j] = min(insert, replace, delete)
      return dp[0][0]

    def minDistance(self, word1: str, word2: str) -> int:
        return self.tab(word1,word2)