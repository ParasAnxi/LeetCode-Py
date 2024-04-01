class Solution:
    def solve(self, nums, ans, index):
      if index >= len(nums):
        ans.append(nums[:])
        return
      for i in range(index, len(nums)):
        nums[i], nums[index] = nums[index], nums[i]
        self.solve(nums, ans, index + 1)
        nums[i], nums[index] = nums[index], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.solve(nums, ans, 0)
        return ans
