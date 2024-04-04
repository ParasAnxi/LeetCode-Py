from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        winodw = {}
        req = len(target)
        curr = 0
        left, right = 0, 0
        mini = float('inf')
        minLeft = 0

        while right < len(s):
            char = s[right]
            winodw[char] = winodw.get(char, 0) + 1
            if char in target and winodw[char] == target[char]:
                curr += 1

            while curr == req and left <= right:
                if right - left + 1 < mini:
                    mini = right - left + 1
                    minLeft = left

                char = s[left]
                winodw[char] -= 1
                if char in target and winodw[char] < target[char]:
                    curr -= 1

                left += 1

            right += 1

        return "" if mini == float('inf') else s[minLeft:minLeft+mini]
