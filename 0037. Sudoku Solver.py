class Solution:
    def isPossible(self, board: List[List[str]], row: int, col: int, c: str) -> bool:
      for i in range(9):
        if board[i][col] == c:
          return False
        if board[row][i] == c:
          return False
        if board[3 * (row // 3) + i//3][3*(col//3)+i % 3] == c:
          return False
      return True

    def solve(self, board: List[List[str]]) -> bool:
      for i in range(9):
        for j in range(9):
          if board[i][j] == '.':
            for ch in range(ord('1'), ord('9') + 1):
              c = chr(ch)
              if self.isPossible(board, i, j, c):
                board[i][j] = c
                if self.solve(board):
                  return True
                else:
                  board[i][j] = '.'
            return False
      return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
