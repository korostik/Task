# https://leetcode.com/problems/fruits-into-baskets-iii/description/

class Solution:
    def numOfUnplacedFruits(self, fruits, baskets) -> int:
        len_baskets = len(baskets)

        for i in range(len_baskets):
            baskets[i] = [baskets[i], i]
        baskets.sort()

        ct = 0
        while 2 ** ct < len_baskets:
            ct += 1
        baskets_for_tree = baskets
        for i in range(2 ** ct - len_baskets):
            baskets_for_tree = [[-1, 10**9 + 1]] + baskets_for_tree

        ans = 0        

        tree = self.CreateTree(baskets_for_tree)
        for elem in fruits:
            tree, ans = self.search(elem, baskets, ans, tree, 2 ** ct - len_baskets)
        return ans

    def search(self, elem, baskets, ans, tree, left2):
        l = 0
        r = len(baskets) - 1
        mid = (l + r) // 2
        while l <= r:
            if baskets[mid][0] == elem:
                l = mid
                break
            elif baskets[mid][0] < elem:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r) // 2

        if baskets[l:] == []:
            ans += 1
            return tree, ans

        tree, ans = self.minRange(l, tree, ans, left2)

        return tree, ans
    

    def CreateTree(self, baskets):
        tree = ["Empty"] * len(baskets) + baskets
        
        #дерево [вместимость  корзины, номер корзины в списке корзин,  номер корзины в списке tree]
        for i in range(len(baskets), len(tree)):
            tree[i] = [tree[i][0], tree[i][1], i]


        right = 2 * len(baskets) - 1
        for i in range(right, 0, -2):
            if tree[1] != "Empty":
                break
            a = tree[i][1]
            b = tree[i - 1][1]
            if min(a, b) == a:
                tree[i // 2] = tree[i]
            else:
                tree[i // 2] = tree[i - 1]
        return tree
    
    
    
    def minRange(self, left, tree, main_ans, left2):
        left = len(tree) // 2 + left + left2
        right = len(tree) - 1
        del_ind = -1
        ans = 10**9
        while left <= right:
            if left % 2 != 0:
                if ans > tree[left][1]:
                    ans = tree[left][1]
                    del_ind = tree[left][2]
                
            if right % 2 == 0:
                if ans > tree[left][1]:
                    ans = tree[left][1]
                    del_ind = tree[right][2]
            
            left = (left + 1) // 2
            right = (right - 1) // 2
        if del_ind  == -1:
            return tree, main_ans+1
        tree = self.fixtree(tree, del_ind)
        return tree, main_ans + (ans == 10 ** 9)
    
    def fixtree(self, tree, del_ind):
        tree[del_ind][1] =  10**9 + 1
        tek =  del_ind // 2
        while tek > 0:
            a = tree[tek * 2]
            b = tree[tek * 2 + 1]
            if a[1] < b[1]:
                tree[tek] = a
            else:
                tree[tek] = b
            tek //= 2
        return tree
