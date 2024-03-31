class Solution:
    def LPS(self, pattern: str) -> List[int]:
      n = len(pattern)
      lps = [0] * n
      LEN = 0
      i = 1
      while i < n:
        if pattern[i] == pattern[LEN]:
          LEN += 1
          lps[i] = LEN
          i += 1
        else:
          if LEN != 0:
            LEN = lps[LEN - 1]
          else:
            lps[i] = 0
            i += 1
      return lps

    def strStr(self, haystack: str, needle: str) -> int:
      if not needle:
        return 0

      lps = self.LPS(needle)
      i, j = 0, 0

      while i < len(haystack):
        if haystack[i] == needle[j]:
          i += 1
          j += 1

        if j == len(needle):
          return i - j

        if i < len(haystack) and haystack[i] != needle[j]:
          if j != 0:
            j = lps[j - 1]
          else:
            i += 1
      return -1
