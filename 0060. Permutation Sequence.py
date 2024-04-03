class Solution:
    def getPermutation(self, n: int, k: int) -> str:
      ans = ""
      fact = [1] * (n + 1)
      for i in range(1, n+1):
        fact[i] = i * fact[i - 1]
      digits = [str(i) for i in range(1, n + 1)]
      k -= 1

      for i in range(n, 0, -1):
        index = k // fact[i - 1]
        ans += digits[index]
        digits.pop(index)
        k %= fact[i - 1]
        if k == 0:
          ans += "".join(digits)
          break
      return ans
