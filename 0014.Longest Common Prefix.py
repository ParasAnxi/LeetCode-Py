class Solution:
    def isLcp(self, strs: List[str], length: int) -> bool:
      str1 = strs[0][:length]
      for i in range(1, len(strs)):
        if not strs[i].startswith(str1):
          return False
      return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
      if not strs:
        return ""
      minLen = float('inf')
      for st in strs:
        x = len(st)
        minLen = min(minLen, x)

      left, right = 0, minLen
      while left < right:
        mid = (left + right) // 2
        if self.isLcp(strs, mid + 1):
          left = mid + 1
        else:
          right = mid
      return strs[0][:left]
