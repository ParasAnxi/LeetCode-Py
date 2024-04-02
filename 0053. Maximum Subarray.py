#kanade algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
          return 0
        sum = -2**32
        curr = 0
        for i in range(len(nums)):
          curr += nums[i]
          if sum < curr:
            sum = curr
          if curr < 0:
            curr = 0
        return sum
