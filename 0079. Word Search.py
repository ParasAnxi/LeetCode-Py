class Solution:
    def solve(self, board, word, i, j, k):
      n = len(board)
      m = len(board[0])
      if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[k]:
        return False
      if k == len(word) - 1:
        return True
      temp = board[i][j]
      board[i][j] = '#'
      ans = (self.solve(board, word, i+1, j, k+1) or
             self.solve(board, word, i-1, j, k+1) or
             self.solve(board, word, i, j+1, k+1) or
             self.solve(board, word, i, j-1, k+1))
      board[i][j] = temp
      return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        for i in range(n):
          for j in range(m):
            if self.solve(board, word, i, j, 0):
              return True
        return False
