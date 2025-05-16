#https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, a, x):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] + a[j] == x:
                    return [i, j]
