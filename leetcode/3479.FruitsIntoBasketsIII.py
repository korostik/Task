# https://leetcode.com/problems/fruits-into-baskets-iii/description/

import math
max_number = 10** 9
class Solution:
    def numOfUnplacedFruits(self, fruits, baskets) -> int:
        len_baskets = len(baskets)

        for i in range(len_baskets):
            baskets[i] = [baskets[i], i]
        baskets.sort()

        cd = 2 ** math.ceil(math.log(len(baskets), 2)) - len(baskets)

        baskets_for_tree = baskets
        for i in range(cd):
            baskets_for_tree = [[-1, max_number + 1]] + baskets_for_tree

        ans = 0
        tree = self.CreateTree(baskets_for_tree)

        self.baskets = baskets
        self.tree = tree
        self.ans = ans

        for elem in fruits:
            # TODO: we have some understandable problems
            tree, ans = self.search(elem, cd)

        # TODO: The ans is one more
        return ans

    def search(self, elem, left2):
        l = 0
        r = len(self.baskets) - 1
        mid = (l + r) // 2
        while l <= r:
            if self.baskets[mid][0] == elem:
                l = mid
                break
            elif self.baskets[mid][0] < elem:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r) // 2

        if self.baskets[l:] == []:
            self.ans += 1
            return self.tree, self.ans

        self.tree, self.ans = self.minRange(l, self.ans, left2)

        return self.tree, self.ans
    

    def CreateTree(self, baskets):
        tree = ["Empty"] * len(baskets) + baskets
        
        #дерево [вместимость  корзины, номер корзины в списке корзин,  номер корзины в списке tree]
        for i in range(len(baskets), len(tree)):
            tree[i] = [tree[i][0], tree[i][1], i]


        for i in range(len(tree) - 1, 1, -2):
            if min(tree[i][1], tree[i - 1][1]) == tree[i][1]:
                tree[i // 2] = tree[i]
            else:
                tree[i // 2] = tree[i - 1]
        return tree
    
    
    
    def minRange(self, left, main_ans, left2):
        left = len(self.tree) // 2 + left + left2
        right = len(self.tree) - 1
        del_ind = -1
        ans = max_number
        while left <= right:
            if left % 2 != 0:
                if ans > self.tree[left][1]:
                    ans = self.tree[left][1]
                    del_ind = self.tree[left][2]
                
            if right % 2 == 0:
                if ans > self.tree[left][1]:
                    ans = self.tree[left][1]
                    del_ind = self.tree[right][2]
            
            left = (left + 1) // 2
            right = (right - 1) // 2
        if del_ind  == -1:
            return self.tree, main_ans+1
        self.tree = self.fixtree(self.tree, del_ind)
        return self.tree, main_ans + (ans == max_number)
    
    def fixtree(self, tree, del_ind):
        tree[del_ind][1] =  max_number + 1
        tek =  del_ind // 2
        while tek > 0:
            if tree[tek * 2][1] < tree[tek * 2 + 1][1]:
                tree[tek] = tree[tek * 2]
            else:
                tree[tek] = tree[tek * 2 + 1]
            tek //= 2
        return tree
