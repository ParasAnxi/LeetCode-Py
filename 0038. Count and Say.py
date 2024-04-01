class Solution:
    def countAndSay(self, n: int) -> str:
      ans = "1"
      for i in range(2, n + 1):
        temp = ""
        count = 1
        for j in range(1, len(ans)):
          if ans[j] == ans[j - 1]:
            count += 1
          else:
            temp += str(count) + ans[j - 1]
            count = 1
        temp += str(count) + ans[-1]
        ans = temp
      return ans
