# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/submissions/?envType=problem-list-v2&envId=queue

class Solution:
    def countStudents(self, st, sand):
        flag = True
        ist = 0
        isand = 0
        count = 0
        while flag and ist != len(st):
            if st[ist] != sand[isand]:
                st.append(st[ist])
                ist += 1
            else:
                ist += 1
                isand += 1
            count += 1
            if count == 5050: #худший случай с запасом 100 + 99 + 88+...+1
                flag = False
        return len(sand) - isand
