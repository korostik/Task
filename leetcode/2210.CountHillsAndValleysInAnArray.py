# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/?envType=daily-question&envId=2025-07-27

class Solution:
    def countHillValley(self, a):
        a = self.new_a(a)
        ans = 0
        for i in range(1, len(a) - 1):
            if a[i - 1] <= a[i] and a[i] >= a[i + 1]:
                ans += 1
            elif a[i - 1] >= a[i] and a[i] <= a[i + 1]:
                ans += 1
        return ans
    

    def new_a(self, a):
        new_a = [0] * len(a)
        d = {}
        ni = 0
        for i in range(len(a)):
            if d.get(a[i]) == None or i - d[a[i]] > 1:
                new_a[ni] = a[i]
                ni += 1

            d[a[i]] = i
        
        return new_a[:ni]
