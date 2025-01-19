class Solution(object):
    def searchInsert(self, a, x):
        l = 0
        r = len(a) - 1
        OK = True
        while r -  l > 1:
            mid = (l + r) // 2
            if x < a[mid]:
                r = mid
            elif x >= a[mid]:
                l = mid
        if a[r] == x:
            return r
        elif a[l] == x:
            return l
        elif a[r] < x:
            return r + 1
        elif a[l] > x and l > 0:
            return l - 1
        elif a[l] < x:
            return r
        else:
            return l


        