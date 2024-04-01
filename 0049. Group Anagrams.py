class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
          st = ''.join(sorted(word))
          if st not in map:
            map[st] = []
          map[st].append(word)
        ans = []
        for x in map.values():
          ans.append(x)
        return ans
