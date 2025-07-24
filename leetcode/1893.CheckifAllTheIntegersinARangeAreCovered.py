# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/?envType=problem-list-v2&envId=prefix-sum

class Solution(object):
    def isCovered(self, ranges, left, right):
        a = set([i for i in range(left, right + 1)])
        b = []
        for i in range(len(ranges)):
            b.extend([i for i in range(ranges[i][0], ranges[i][1] + 1)])
        b = set(b)
        if b & a == a:
            return True
        else:
            return False
