class Solution(object):
    def isPalindrome(self, s):
        ans = ""
        s = s.lower()
        for i in range(len(s)):
            if s[i] in "qwertyuiopasdfghjklzxcvbnm0123456789":
                ans += s[i]
        return ans == ans[::-1]
        


        