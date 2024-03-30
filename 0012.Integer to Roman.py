class Solution:
    def intToRoman(self, num: int) -> str:
      mp = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9),("V", 5), ("IV", 4), ("I", 1)]
      ans = ""
      for sym, val in mp:
         while num >= val:
            ans += sym
            num -= val 
      return ans