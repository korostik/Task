#https://leetcode.com/problems/range-product-queries-of-powers/description/?envType=daily-question&envId=2025-08-11

import math
max_number = 10**9 + 7
class Solution:
    def productQueries(self, n: int, x):
        product = self.CreateProduct(n)
        cd = 2 ** math.ceil(math.log(len(product), 2)) - len(product)
        for i in range(cd):
            product.insert(0, 1)

        tree = self.CreateTree(product)
        ans = []
        for i in range(len(x)):
            ans.append(self.proizRange(tree, x[i][0], x[i][1], cd))
        return ans

    def proizRange(self, tree, l, r, cd):
        left = len(tree) // 2 + l + cd
        right = len(tree) // 2 + r + cd
        ans = 1
        while left <= right:
            if left % 2 != 0:
                ans *= tree[left]
            if right % 2 == 0:
                ans *= tree[right]
            
            left = (left + 1) // 2
            right = (right - 1) // 2
        return ans % max_number


    def CreateProduct(self, n):
        product = []
        maxct = 2 ** int(math.log(n, 2))

        while maxct != 0:
            if n - maxct >= 0:
                n -= maxct
                product.append(maxct)
            maxct //= 2

        return product[::-1]
    
    def CreateTree(self, product):
        tree = ["Empty"] * len(product) + product
        for i in range(len(tree) - 1, 1, -2):
            tree[i // 2] = tree[i] * tree[i - 1]
        return tree
