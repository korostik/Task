#https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=prefix-sum

class Solution(object):            
    def minSubArrayLen(self, x, a):
        left = 0
        right = 0
        now_sum = 0
        minilen = 10**10
        for i in range(len(a)):
            if now_sum + a[i] < x:
                now_sum += a[i]
                right += 1
            else:
                sum_left = a[left]
                now_sum += a[i]
                while now_sum - sum_left >= x:
                    now_sum -= a[left]
                    left += 1
                    sum_left = a[left]
                minilen = min(minilen, right - left + 1)
                right += 1
                
        if sum(a) < x:
            return 0
        return minilen
