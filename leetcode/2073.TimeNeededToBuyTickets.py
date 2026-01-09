# https://leetcode.com/problems/time-needed-to-buy-tickets/submissions/1879972665/?envType=problem-list-v2&envId=queue

class Solution:
    def timeRequiredToBuy(self, a, k) -> int:
        a[k] = [a[k], 'NEED']
        flag = True
        tek = 0
        count = 0
        while flag:
            if type(a[tek]) == int:
                if a[tek] != 1:
                    a.append(a[tek] - 1)
                count += 1
            else:
                if a[tek][0] == 1:
                    flag = False
                else:
                    a[tek][0] -= 1
                    a.append(a[tek])
                count += 1
            tek += 1
        return count
