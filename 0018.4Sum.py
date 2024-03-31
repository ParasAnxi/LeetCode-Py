class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)

        for i in range(n - 3):
          if i > 0 and nums[i] == nums[i - 1]:
            continue
          for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
              continue
            s, e = j + 1, n - 1
            while s < e:
              currSum = nums[i] + nums[j] + nums[s] + nums[e]
              if currSum == target:
                ans.add((nums[i], nums[j], nums[s], nums[e]))
                s += 1
                e -= 1
                while s < e and nums[s] == nums[s - 1]:
                  s += 1
                while s < e and nums[e] == nums[e + 1]:
                  e -= 1
              elif currSum < target:
                s += 1
              else:
                e -= 1

        return [list(i) for i in ans]
