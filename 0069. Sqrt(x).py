class Solution:
    def bs(self, x: int) -> int:
      s = 0
      e = x
      ans = -1
      mid = s + (e - s) // 2

      while s <= e:
        sq = mid * mid
        if sq == x:
          return mid
        elif sq < x:
          ans = mid
          s = mid + 1
        else:
          e = mid - 1
        mid = s + (e - s) // 2
      return ans

    def mySqrt(self, x: int) -> int:
      return self.bs(x)
