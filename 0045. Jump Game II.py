class Solution:
    def jump(self, nums: List[int]) -> int:
      n = len(nums)
      reach = 0
      steps = 0
      jumps = 0

      for i in range(n - 1):
        reach = max(reach, i + nums[i])
        if i == steps:
          steps = reach
          jumps += 1
      return jumps
