class Solution:
    def canJump(self, nums: List[int]) -> bool:
       n = len(nums)
       maxi = 0
       for i in range(n):
        maxi = max(maxi, i + nums[i])
        if maxi >= n - 1:
          return True
        if maxi == i and nums[i] == 0:
          return False
       return False
        