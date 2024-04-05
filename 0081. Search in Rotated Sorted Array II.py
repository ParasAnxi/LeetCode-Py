class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        s, e = 0, len(nums) - 1
        while s <= e:
          mid = (s + e) // 2
          if nums[mid] == target:
            return True
          if nums[s] == nums[mid] and nums[e] == nums[mid]:
            s += 1
            e -= 1
          elif nums[s] <= nums[mid]:
            if nums[s] <= target and nums[mid] > target:
              e = mid - 1
            else:
              s = mid + 1
          else:
            if nums[mid] < target and nums[e] >= target:
              s = mid + 1
            else:
              e = mid - 1
        return False
