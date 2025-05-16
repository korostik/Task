#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1
        
