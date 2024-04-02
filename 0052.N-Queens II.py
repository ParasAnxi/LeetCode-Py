class Solution:
    def isSafe(self, row, col, board):
      x, y = row, col
      while y >= 0:
        if board[x][y] == 'Q':
          return False
        y -= 1
      x, y = row, col
      while x >= 0 and y >= 0:
        if board[x][y] == 'Q':
          return False
        x -= 1
        y -= 1
      x, y = row, col
      while x < len(board) and y >= 0:
        if board[x][y] == 'Q':
          return False
        x += 1
        y -= 1
      return True

    def solve(self, col, board):
      if col == len(board):
        return 1
      count = 0
      for row in range(len(board)):
        if self.isSafe(row, col, board):
          board[row][col] = 'Q'
          count += self.solve(col + 1, board)
          board[row][col] = '.'
      return count

    def totalNQueens(self, n: int) -> int:
        board = [['.' for _ in range(n)] for _ in range(n)]
        return self.solve(0, board)
