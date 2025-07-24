# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=prefix-sum

class Solution(object):            
    def minSubArrayLen(self, x, a):
        left = 0
        right = 0
        now_sum = 0
        minilen = 10**10
        for i in range(len(a)):
            now_sum += a[i]
            if now_sum >= x:
                sum_left = a[left]
                while now_sum - sum_left >= x:
                    now_sum -= a[left]
                    left += 1
                    sum_left = a[left]
                minilen = min(minilen, right - left + 1)
            right += 1

        if now_sum < x:
            return 0
        return minilen
