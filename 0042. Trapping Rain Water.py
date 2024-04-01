class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right, l, r, ans = 0, n - 1, 0, 0, 0
        while left <= right:
          if height[left] <= height[right]:
            if l < height[left]:
              l = height[left]
            else:
              ans += l - height[left]
            left += 1
          else:
            if r < height[right]:
              r = height[right]
            else:
              ans += r - height[right]
            right -= 1
        return ans
