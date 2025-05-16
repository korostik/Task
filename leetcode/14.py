//https://leetcode.com/problems/longest-common-prefix/description/
class Solution(object):
    def longestCommonPrefix(self, a):
        s = ""
        index = 0
        OK = True
        while OK:
            cool = ""
            for j in range(len(a)):
                if index <= len(a[j]) - 1:
                    cool += a[j][index]
                else:
                    OK = False
            if OK:
                if cool == cool[0] * len(cool):
                    index += 1
                    s += cool[0]
                else:
                    OK = False
        return s
