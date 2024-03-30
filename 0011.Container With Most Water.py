class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left , right = 0, n - 1
        area = float("-inf")
        while left <= right:
            mini = min(height[left], height[right])
            area = max(area, mini * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area