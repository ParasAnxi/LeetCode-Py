class Solution:
    def solve(self, c, target, ans, output, index):
      if target < 0:
        return
      if target == 0:
        ans.append(output[:])
        return
      if index == len(c):
        return
      self.solve(c, target, ans, output, index+1)
      output.append(c[index])
      self.solve(c, target - c[index], ans, output, index)
      output.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.solve(candidates, target, ans, [], 0)
        return ans
