class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
      ans = []
      i = 0
      width = 0
      curLine = []

      while i < len(words):
        curWord = words[i]
        if width + len(curWord) <= maxWidth:
          curLine.append(curWord)
          width += len(curWord) + 1
          i += 1
        else:
          spaces = maxWidth - width + len(curLine)
          added = 0
          j = 0
          while added < spaces:
            if j >= len(curLine) - 1:
              j = 0
            curLine[j] += " "
            added += 1
            j += 1
          line = "".join(curLine)
          ans.append(line)
          curLine = []
          width = 0

      for word in range(len(curLine) - 1):
        curLine[word] += " "
      curLine[-1] += " " * (maxWidth - width + 1)

      lastLine = "".join(curLine)
      ans.append(lastLine)

      return ans
