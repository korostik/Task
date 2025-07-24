# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/?envType=problem-list-v2&envId=prefix-sum

class Solution(object):
    def minStartValue(self, a):
        pre = []
        k = 0
        for i in range(len(a)):
            k += a[i]
            pre.append(k)
        mini = a[0]
        flag = True
        for i in range(len(pre)):
            if pre[i] <= mini and pre[i] < 0:
                mini = pre[i]
                flag = False
        if flag:
            return 1
        return(abs(mini) + 1)
