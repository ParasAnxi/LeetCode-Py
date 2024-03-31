class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      seen = set()
      for i in range(9):
        for j in range(9):
          if board[i][j] == '.':
            continue
          row = f'{board[i][j]} row {i}'
          col = f'{board[i][j]} column {j}'
          box = f'{board[i][j]} box {i // 3, j // 3}'
          if (row in seen) or (col in seen) or (box in seen):
            return False
          seen.add(row)
          seen.add(col)
          seen.add(box)
      return True
