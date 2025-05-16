#https://leetcode.com/problems/roman-to-integer/description/
class Solution(object):
    def romanToInt(self, s):
        s += "O"
        d = {}
        d["O"] = 0
        d["I"] = 1
        d["V"] = 5
        d["X"] = 10
        d["L"] = 50
        d["C"] = 100
        d["D"] = 500
        d["M"] = 1000
        i = 0
        count = 0
        while i != len(s) - 1:
            if d[s[i]] >= d[s[i + 1]]:
                count += d[s[i]]
                i += 1
            else:
                count += d[s[i + 1]] - d[s[i]]
                i += 2
        return count
