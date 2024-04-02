class Solution:
    def isSafe(self, i, j, board, n):
      x, y = i, j
      while y >= 0:
        if board[x][y] == 'Q':
          return False
        y -= 1

      x, y = i, j
      while y >= 0 and x >= 0:
        if board[x][y] == 'Q':
          return False
        x -= 1
        y -= 1

      x, y = i, j
      while x < n and y >= 0:
        if board[x][y] == 'Q':
          return False
        x += 1
        y -= 1

      return True

    def solve(self, col, board, ans, n):
      if col == n:
        ans.append(["".join(row) for row in board])
        return

      for i in range(n):
        if self.isSafe(i, col, board, n):
          board[i][col] = 'Q'
          self.solve(col + 1, board, ans, n)
          board[i][col] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans
