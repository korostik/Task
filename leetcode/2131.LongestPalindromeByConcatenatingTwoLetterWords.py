# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/?envType=daily-question&envId=2025-05-26

class Solution:
    def longestPalindrome(self, a):
        d1 = {} #different sings 1
        d2 = {} #different sings which are reversed
        d3 = {} #same sings
<<<<<<< HEAD
=======

>>>>>>> c45bcf2 (update to merge pull request)
        for i in range(len(a)):
            s = a[i]
            if s[0] == s[1]:
                d3[s] = d3.get(s, 0) + 1
            else:
                value = d1.get(s[::-1])
                if value is not None:
                    d2[s] = d2.get(s, 0) + 1
                else:
                    d1[s] = d1.get(s, 0) + 1
        ans = 0
        for k, v in d1.items():
            value = d2.get(k[::-1], 0)
            ans += min(value, v) * 4

        flag = -1
        for k, v in d3.items():
            if v % 2 == 1 and v > 1:
                ans += (v - 1) * 2
                flag = 0
            elif v % 2 == 0:
                ans += v * 2
            else:
                flag = 0
        return ans + (flag == 0) * 2
