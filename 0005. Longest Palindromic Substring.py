class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '^#' + '#'.join(s) + '#$'
        n = len(t)
        p = [0] * n
        c = r = 0
        for i in range(1 , n - 1):
            if i < r:
                p[i] = min(p[2 * c - i], r - i)
            while t[i + 1 + p[i]] == t[i - i - p[i]]:
                p[i] += 1
            if p[i] + i > r:
                r = p[i] + i
                c = i
        maxLen = max(p)
        center = p.index(maxLen)
        start = (center - maxLen) // 2
        return s[start:start + maxLen]