# https://leetcode.com/problems/continuous-subarray-sum/?envType=problem-list-v2&envId=prefix-sum

class Solution(object):
    def checkSubarraySum(self, a, k):
        prefix = [0]
        summi = 0
        for i in range(len(a)):
            summi += a[i]
            prefix.append(summi)

        d = {}
        for i in range(len(prefix)):
            if d.get(prefix[i] % k) == None:
                d[prefix[i]%k] = -1
            if d[prefix[i] % k] == -1:
                d[prefix[i] % k] = i
            else:
                if i - d[prefix[i] % k] >= 2:
                    return True
        return False
