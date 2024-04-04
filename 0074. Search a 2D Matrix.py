class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
          return False

        row = len(matrix)
        col = len(matrix[0])
        start = 0
        end = row * col - 1

        while start <= end:
            mid = start + (end - start) // 2
            element = matrix[mid // col][mid % col]

            if element == target:
                return True
            elif element < target:
                start = mid + 1
            else:
                end = mid - 1

        return False
