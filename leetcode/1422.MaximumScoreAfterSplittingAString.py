# https://leetcode.com/problems/maximum-score-after-splitting-a-string/?envType=problem-list-v2&envId=prefix-sum

class Solution(object):
    def maxScore(self, s):
        a = list(map(int, s.replace("", " ").split()))
        count0 = 0
        count1 = sum(a)
        ans = 0
        for i in range(len(a) - 1):
            if a[i] == 0:
                count0 += 1
            else:
                count1 -= 1
            ans = max(ans, count0 + count1)
        return ans
    