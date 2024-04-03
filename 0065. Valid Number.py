class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
          return False
        n = len(s)
        i = 0
        isNum = False

        while i < n and s[i].isspace():
          i += 1

        if i < n and (s[i] == "+" or s[i] == "-"):
          i += 1

        while i < n and s[i].isdigit():
          i += 1
          isNum = True

        if i < n and s[i] == ".":
          i += 1
          while i < n and s[i].isdigit():
            i += 1
            isNum = True

        if isNum and i < n and (s[i] == "e" or s[i] == "E"):
          i += 1

          if i < n and (s[i] == "+" or s[i] == "-"):
            i += 1

          if i < n and s[i].isdigit():
            while i < n and s[i].isdigit():
              i += 1
              isNum = True
          else:
            return False

        while i < n and s[i].isspace():
          i += 1

        return isNum and i == n
