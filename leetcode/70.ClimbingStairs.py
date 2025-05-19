# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n):
        a = [1, 2, 3]
        if n < 4:
            return(a[n - 1])
        else:
            for i in range(3, n):
                a.append(a[i - 1] + a[i - 2])
            return(a[n - 1])
