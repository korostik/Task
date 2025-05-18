#https://leetcode.com/problems/search-insert-position/description/
class Solution(object):
    def searchInsert(self, a, x):
        l = 0
        r = len(a) - 1
        while l <= r:
            mid = (l + r) // 2
            if a[mid] == x:
                return mid
            elif x < a[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l 
