class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
          return 0

        n = len(matrix)
        m = len(matrix[0])
        heights = [0] * (m + 1)
        maxi = 0

        for row in matrix:
          for j in range(m):
            heights[j] = heights[j] + 1 if row[j] == '1' else 0

          stack = [-1]
          for j in range(m + 1):
            while heights[j] < heights[stack[-1]]:
              height = heights[stack.pop()]
              width = j - stack[-1] - 1
              maxi = max(maxi, height * width)
            stack.append(j)

        return maxi
