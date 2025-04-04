class Solution(object):
    def maxProfit(self, a):
        ans = 0
        maxi = -1
        mini = 10**4+1
        ind_mini = 0
        ind_maxi = 0
        for i in range(len(a)):
            x = a[i]
            if ind_mini < ind_maxi and i != 0:
                ans = max(ans, a[ind_maxi] - a[ind_mini])
            elif ind_mini > ind_maxi:
                ind_maxi = -1
                maxi = -1
            if maxi < x:
                maxi = x
                ind_maxi = i
            if mini > x:
                mini = x
                ind_mini = i
            
        if ind_mini < ind_maxi and i != 0:
            ans = max(ans, a[ind_maxi] - a[ind_mini])
        return ans



