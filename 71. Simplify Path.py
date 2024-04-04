class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        comp = path.split('/')

        for c in comp:
          if c == '' or c == '.':
            continue
          elif c == '..':
            if stack:
              stack.pop()
          else:
              stack.append(c)

        ans = '/' + '/'.join(stack)
        return ans
