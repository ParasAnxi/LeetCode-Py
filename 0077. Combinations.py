class Solution:
    def solve(self, n, k, index, ans, output):
      if len(output) == k:
        ans.append(output[:])
        return

      for i in range(index, n + 1):
        output.append(i)
        self.solve(n, k, i+1, ans, output)
        output.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.solve(n, k, 1, ans, [])
        return ans
