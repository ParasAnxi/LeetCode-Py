class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
          return "0"
        n1, n2 = len(num1), len(num2)
        ans = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, - 1):
          for j in range(n2 - 1, -1, -1):
            pro = int(num1[i]) * int(num2[j])
            carry = pro // 10
            digit = pro % 10
            ans[i + j + 1] += digit
            ans[i + j] += carry
            if ans[i + j + 1] >= 10:
              ans[i + j] += ans[i + j + 1] // 10
              ans[i + j + 1] %= 10

        res = ""
        i = 0
        while i < len(ans) and ans[i] == 0:
          i += 1
        while i < len(ans):
          res += str(ans[i])
          i += 1
        return res
