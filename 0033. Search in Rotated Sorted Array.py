class Solution:
    def bs(self, nums, s, e, target):
      while s <= e:
        mid = s + (e - s) // 2
        if nums[mid] == target:
          return mid
        elif target < nums[mid]:
          e = mid - 1
        else:
          s = mid + 1
      return -1

    def pivot(self, nums):
      left, right = 0, len(nums) - 1
      while left < right:
        mid = left + (right - left) // 2
        if nums[0] <= nums[mid]:
          left = mid + 1
        else:
          right = mid
      return left

    def search(self, nums: List[int], target: int) -> int:
      p = self.pivot(nums)
      n = len(nums)
      if nums[p] <= target <= nums[n - 1]:
        return self.bs(nums, p, n-1, target)
      else:
        return self.bs(nums, 0, p-1, target)
