class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0

        m = {}

        for r in range(len(s)):
            while s[r] in m:
                m.pop(s[l])
                l += 1
            m[s[r]] = 1
            max_len = max(max_len, r - l + 1)
        return max_len


        