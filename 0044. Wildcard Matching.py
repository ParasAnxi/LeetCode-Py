#TLE
class Solution:
    def mem(self, s, p, i, j):
      dp = {}
      if (i, j) in dp:
        return dp[(i, j)]
      if i == 0 and j == 0:
        return True
      if i > 0 and j == 0:
        return False
      if i == 0 and j > 0:
        return all(p[k - 1] == '*' for k in range(1, j+1))

      if s[i - 1] == p[j - 1] or p[j - 1] == '?':
        dp[(i, j)] = self.mem(s, p, i - 1, j - 1)
      elif p[j - 1] == '*':
        dp[(i, j)] = self.mem(s, p, i - 1, j) or self.mem(s, p, i, j - 1)
      else:
        dp[(i, j)] = False
      return dp[(i, j)]

    def isMatch(self, s: str, p: str) -> bool:
      return self.mem(s, p, len(s), len(p))


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      prev = [True] + [False] * len(p)
      for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
          prev[j] = True
        else:
          break

      for i in range(1, len(s) + 1):
        curr = [False] * (len(p) + 1)
        for j in range(1, len(p) + 1):
          if s[i - 1] == p[j - 1] or p[j - 1] == '?':
            curr[j] = prev[j - 1]
          elif p[j - 1] == '*':
            curr[j] = prev[j] or curr[j - 1]
        prev = curr

      return prev[-1]
