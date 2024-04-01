class Solution:
    def solve(self, nums, st, index):
      if index == len(nums):
        st.add(tuple(nums))
        return
      for i in range(index, len(nums)):
        nums[i], nums[index] = nums[index], nums[i]
        self.solve(nums, st, index + 1)
        nums[i], nums[index] = nums[index], nums[i]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        st = set()
        self.solve(nums, st, 0)
        for x in st:
          ans.append(list(x))
        return ans
