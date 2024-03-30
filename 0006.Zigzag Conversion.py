class Solution:
    def convert(self, s: str, n: int) -> str:
      if n == 1:
          return s
      arr = [''] * n
      row = 0
      down = True

      for ch in s:
        arr[row] += ch
        if row == 0:
          down = True
        elif row == n - 1:
          down = False
        row = row + 1 if down else row - 1
      ans = ''.join(arr)
      return ans
