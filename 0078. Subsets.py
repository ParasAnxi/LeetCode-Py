class Solution:
    def solve(self, nums, index, ans, output):
      if index >= len(nums):
        ans.append(output[:])
        return
      self.solve(nums, index+1, ans, output)
      ele = nums[index]
      output.append(ele)
      self.solve(nums, index+1, ans, output)
      output.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.solve(nums, 0, ans, [])
        return ans
