class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.lstrip().rstrip()
        k = s.rfind(" ")
        return len(s[k + 1:])
        

        