class Solution:
    def first(self, nums, target):
      s, e = 0, len(nums) - 1
      while s <= e:
        mid = s + (e - s) // 2
        if nums[mid] < target:
          s = mid + 1
        else:
          e = mid - 1
      return s

    def last(self, nums, target):
      s, e = 0, len(nums) - 1
      while s <= e:
        mid = s + (e - s) // 2
        if nums[mid] <= target:
          s = mid + 1
        else:
          e = mid - 1
      return e

    def searchRange(self, nums: List[int], target: int) -> List[int]:
      f = self.first(nums, target)
      l = self.last(nums, target)
      if f <= l:
        return [f, l]
      else:
        return [-1, -1]
