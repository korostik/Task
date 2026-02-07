# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        ans = 0
        for i in range(len(s)):
            if d.get(s[i]) == None:
                d[s[i]] = i
            else:
                ans = max(i - l, ans)
                l = max(d[s[i]] + 1, l)
                d[s[i]] = i
        return max(len(s) - l, ans)
