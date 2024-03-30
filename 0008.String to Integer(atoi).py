class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i, sign, ans = 0, 1, 0
        while i < n and s[i] == ' ':
            i += 1
        if i < n and s[i] == '+':
            sign = 1
            i += 1
        elif i < n and s[i] == '-':
            sign = -1
            i += 1
        while i < n and '0' <= s[i] <= '9':
            ans = (ans * 10) + int(s[i])
            if ans * sign > 2**31 - 1:
                return 2**31 - 1
            elif ans * sign < -2**31:
                return -2**31
            i += 1
        return ans * sign
