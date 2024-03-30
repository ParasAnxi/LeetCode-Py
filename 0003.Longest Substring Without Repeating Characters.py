class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, ans = 0, 0 , 0
        mp = {}
        while right < len(s):
            mp[s[right]] = mp.get(s[right],0) + 1
            while mp[s[right]] > 1:
                mp[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans