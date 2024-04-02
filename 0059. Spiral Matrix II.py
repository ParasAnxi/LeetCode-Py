class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0] * n for _ in range(n)]
        curr = 1
        i, j = 0, 0
        left, right, top, bottom = 0, n - 1, 0, n - 1

        while curr <= n * n:
            while curr <= n * n and j <= right:
                arr[i][j] = curr
                curr += 1
                j += 1
            j -= 1
            i += 1
            top += 1

            while curr <= n * n and i <= bottom:
                arr[i][j] = curr
                curr += 1
                i += 1
            i -= 1
            j -= 1
            right -= 1

            while curr <= n * n and j >= left:
                arr[i][j] = curr
                curr += 1
                j -= 1
            j += 1
            i -= 1
            bottom -= 1

            while curr <= n * n and i >= top:
                arr[i][j] = curr
                curr += 1
                i -= 1
            i += 1
            j += 1
            left += 1

        return arr
