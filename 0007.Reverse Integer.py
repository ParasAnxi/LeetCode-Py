class Solution:
    def reverse(self, x: int) -> int:
      INT_MAX = 2 ** 31 - 1
      INT_MIN = -2 ** 31
      ans = 0

      while x != 0:
        if ans > INT_MAX / 10 or ans < INT_MIN / 10:
            return 0
        digit = x % 10 if x > 0 else x % -10
        ans = ans * 10 + digit
        x = math.trunc(x / 10)
      return ans
