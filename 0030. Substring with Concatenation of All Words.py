from collections import defaultdict as DD


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
          return []

        wordLen = len(words[0])
        arrLen = len(words)
        ans = []
        toVisit = DD(int)
        for word in words:
          toVisit[word] += 1

        for i in range(wordLen):
          left, right, count, visited = i, i, 0, DD(int)

          while right + wordLen <= len(s):
            word = s[right:right + wordLen]
            right += wordLen

            if word not in toVisit:
              visited.clear()
              left = right
              count = 0
            else:
              visited[word] += 1
              count += 1
              while visited[word] > toVisit[word]:
                leftWord = s[left:left + wordLen]
                visited[leftWord] -= 1
                count -= 1
                left += wordLen
              if count == arrLen:
                ans.append(left)

        return ans
