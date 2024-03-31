class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        sum = float('inf')
        minDiff = float('inf')
        for i in range(n - 2):
          if i > 0 and nums[i] == nums[i - 1]:
            continue
          j, k = i + 1, n - 1

          while j < k:
            curr_sum = nums[i] + nums[j] + nums[k]
            curr_diff = abs(target - curr_sum)

            if curr_diff < minDiff:
              sum = curr_sum
              minDiff = curr_diff

            if curr_sum < target:
              j += 1
            elif curr_sum > target:
              k -= 1
            else:
              return target
        return sum
