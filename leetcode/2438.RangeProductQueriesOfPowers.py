# https://leetcode.com/problems/range-product-queries-of-powers/description/

import math

max_number = 10**9 + 7


class Solution:
    def productQueries(self, n: int, queries):
        product = self.create_product(n)
        cd = 2 ** math.ceil(math.log(len(product), 2)) - len(product)
        for i in range(cd):
            product.insert(0, 1)

        tree = self.create_tree(product)
        ans = []
        for i in range(len(queries)):
            ans.append(self.product_range(tree, queries[i][0], queries[i][1], cd))
        return ans

    def product_range(self, tree, left, right, cd):
        left_index = len(tree) // 2 + left + cd
        right_index = len(tree) // 2 + right + cd
        ans = 1
        while left_index <= right_index:
            if left_index % 2 != 0:
                ans *= tree[left_index]
            if right_index % 2 == 0:
                ans *= tree[right_index]
            
            left_index = (left_index + 1) // 2
            right_index = (right_index - 1) // 2
        return ans % max_number

    def create_product(self, n):
        product = []
        maxct = 2 ** int(math.log(n, 2))

        while maxct != 0:
            if n - maxct >= 0:
                n -= maxct
                product.append(maxct)
            maxct //= 2

        return product[::-1]
    
    def create_tree(self, product):
        tree = ["Empty"] * len(product) + product
        for i in range(len(tree) - 1, 1, -2):
            tree[i // 2] = tree[i] * tree[i - 1]
        return tree
