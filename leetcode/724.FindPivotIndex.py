# https://leetcode.com/problems/find-pivot-index/description/?envType=problem-list-v2&envId=prefix-sum

class Solution(object):
    def pivotIndex(self, a):
        count = 0
        summi = sum(a)
        for i in range(len(a)):
            if count == summi - count - a[i]:
                return i
            count += a[i]
        return -1
    