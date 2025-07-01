# https://leetcode.com/problems/shifting-letters/submissions/1682565713/?envType=problem-list-v2&envId=prefix-sum

class Solution:
    def shiftingLetters(self, s, a):
        prefix = [0]
        alf = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        summi = 0
        for i in range(len(a)):
            summi += a[i]
            prefix.append(summi % 26)
        
        maxi = prefix[-1]
        j = 0
        ans = ''
        for i in range(len(s)):
            ans += self.sdvig(s[i], alf, maxi - prefix[j])
            j += 1
        return ans

        
    def sdvig(self, l, alf, k):
        l = alf[alf.find(l) + k]
        return l
