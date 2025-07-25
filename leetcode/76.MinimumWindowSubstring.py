# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s, x):
        d_work = {}
        d_have = {}
        for i in range(len(x)):
            d_work[x[i]] = 0
            d_have[x[i]] = d_have.get(x[i], 0) + 1
    
        left = 0
        ans = ""
        count_values = d_work.get(s[0]) != None
        if d_work.get(s[0]) == 0:
            d_work[s[0]] += 1
        count = len(x)
        for i in range(1, len(s)):
            if left == len(s):
                return ""
            
            if count <= count_values:
                if ans == "" or len(s[left:i]) < len(ans):
                    ans = s[left:i]
            
            if d_work.get(s[i]) != None:
                if d_work[s[i]] < d_have[s[i]]:
                    count_values += 1
                d_work[s[i]] += 1
                
            if s[i] == s[left] or d_work.get(s[left]) == None or d_work[s[left]] > d_have[s[left]]:
                flag = True
                while flag:
                    if left == len(s):
                        return ""
                    elif d_work.get(s[left]) == None:
                        left += 1
                    else:
                        if d_work[s[left]] > d_have[s[left]]:
                            d_work[s[left]] -= 1
                            if d_work[s[left]] < d_have[s[left]]:
                                count_values -= 1
                            left += 1
                        else:
                            flag = False
        
        if count <= count_values:
            if ans == "" or len(s[left:i + 1]) < len(ans):
                ans = s[left:i + 1]
        return ans
