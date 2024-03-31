class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
          return 2**31 - 1

        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        div = abs(dividend)
        dis = abs(divisor)
        ans = 0

        while div >= dis:
          temp = dis
          k = 1
          while temp << 1 <= div:
            temp <<= 1
            k <<= 1
          div -= temp
          ans += k
        return ans * sign
