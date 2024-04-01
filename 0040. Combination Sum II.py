class Solution:
    def solve(self, c, target, ans, output, index):
      if target == 0:
        ans.append(output[:])
        return
      for i in range(index, len(c)):
        if i > index and c[i] == c[i - 1]:
          continue
        if c[i] > target:
          break
        output.append(c[i])
        self.solve(c, target - c[i], ans, output, i + 1)
        output.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.solve(candidates, target, ans, [], 0)
        return ans
