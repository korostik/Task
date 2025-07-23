#https://leetcode.com/problems/equal-sum-grid-partition-i/submissions/1682224475/?envType=problem-list-v2&envId=prefix-sum

class Solution(object):
    def canPartitionGrid(self, a):
        n = len(a)
        m = len(a[0])
        prefixi = []
        prefixj = []
        #count prefixi
        sumi = 0
        for i in range(len(a)):
            summi = 0
            for j in range(len(a[i])):
                summi += a[i][j]
            prefixi.append(summi)
            sumi += summi


        #count prefixj
        sumj = 0
        for i in range(m):
            summi = 0
            for j in range(n):
                summi += a[j][i]
            prefixj.append(summi)
            sumj += summi
        # horizantal
        sumh = prefixi[0]
        for i in range(1, n):
            if sumi / 2 == sumh:
                return True
            sumh += prefixi[i]

        #vertikal
        sumv = prefixj[0]
        for i in range(1, m):
            if sumj / 2 == sumv:
                return True
            sumv += prefixj[i]
        return False
