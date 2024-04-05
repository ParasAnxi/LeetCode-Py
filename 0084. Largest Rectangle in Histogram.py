class Solution:
    def nextSmall(self, heights):
      n = len(heights)
      ans = [-1] * n
      stack = []
      stack.append(-1)
      for i in range(n - 1, -1, -1):
        curr = heights[i]
        while stack[-1] != -1 and heights[stack[-1]] >= curr:
          stack.pop()
        ans[i] = stack[-1]
        stack.append(i)
      return ans

    def prevSmall(self, heights):
      n = len(heights)
      ans = [-1] * n
      stack = []
      stack.append(-1)
      for i in range(n):
        curr = heights[i]
        while stack[-1] != -1 and heights[stack[-1]] >= curr:
          stack.pop()
        ans[i] = stack[-1]
        stack.append(i)
      return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prev = self.prevSmall(heights)
        next = self.nextSmall(heights)

        area = float('-inf')
        for i in range(n):
          length = heights[i]
          if next[i] == -1:
            next[i] = n
          breadth = next[i] - prev[i] - 1
          nArea = length * breadth
          area = max(area, nArea)
        return area
