# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/?envType=problem-list-v2&envId=prefix-sum

class Solution(object):
    def minStartValue(self, a):
        pre = []
        k = 0
        for i in range(len(a)):
            k += a[i]
            pre.append(k)
        mini = 1000
        for i in range(len(pre)):
            if pre[i] < mini and pre[i] < 0:
                mini = pre[i]
        if mini == 1000:
            return(1)
        else:
            return(abs(mini) + 1)
        