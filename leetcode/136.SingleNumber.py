# https://leetcode.com/problems/single-number/description/
class Solution(object):
    def singleNumber(self, a):
        d = {}
        for i in range(len(a)):
            d[a[i]] = d.get(a[i], 0) + 1
        for k, v in d.items():
            if v == 1:
                return k
