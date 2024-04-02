class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
          return []
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]

        for i in intervals[1:]:
          if ans[-1][1] >= i[0]:
            ans[-1][1] = max(ans[-1][1], i[1])
          else:
            ans.append(i)
        return ans
