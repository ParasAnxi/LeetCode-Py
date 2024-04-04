class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
          return

        m, n = len(matrix), len(matrix[0])
        rowZero = False
        colZero = False

        for col in range(n):
          if matrix[0][col] == 0:
            rowZero = True
            break

        for row in range(m):
          if matrix[row][0] == 0:
            colZero = True
            break

        for row in range(1, m):
          for col in range(1, n):
            if matrix[row][col] == 0:
              matrix[0][col] = 0
              matrix[row][0] = 0

        for row in range(1, m):
          for col in range(1, n):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
              matrix[row][col] = 0

        if rowZero:
          for col in range(n):
            matrix[0][col] = 0

        if colZero:
          for row in range(m):
            matrix[row][0] = 0
