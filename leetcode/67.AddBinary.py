#https://leetcode.com/problems/add-binary/description/
class Solution(object):
    def addBinary(self, a, b):
        ans = bin(int(a, 2) + int(b, 2))[2:]
        return ans
        
