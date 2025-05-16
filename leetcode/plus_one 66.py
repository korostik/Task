#https://leetcode.com/problems/plus-one/description/
class Solution(object):
    def plusOne(self, a):
        a = int(''.join(map(str, a)))
        a = a + 1
        ans = []
        while a > 0:
            ans.append(a % 10)
            a //= 10
        return ans[::-1]
