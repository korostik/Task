# https://leetcode.com/problems/pascals-triangle-ii/description/
class Solution(object):
    def getRow(self, n):
        a = []
        c = -1
        n +=1
        for i in range(n):
            if c == -1:
                a.append([1])
            elif c == 0:
                a.append([1, 1])
            else:
                a.append([1] + [0] * c + [1])
            c += 1
        
        for i in range(n):
            k = a[i]
            for j in range (len(k)):
                if a[i][j] != 1:
                    a[i][j] = a[i - 1][j] + a[i - 1][j - 1]
        return a[n - 1]
