import math
class Solution:
    def maxSlidingWindow(self, a: list[int], k) -> list[int]:
        cd = 2 ** math.ceil(math.log(len(a), 2)) - len(a)
        a_for_tree = a.copy()
        for i in range(cd):
            a_for_tree = [-10**5] + a_for_tree
        tree = self.CreateTree(a_for_tree)
        ans = []
        for i in range(len(a) - k + 1):
            ans.append(self.maxRange(tree, i, i + k - 1, cd))
        return ans
    
    def CreateTree(self, a):
        tree = ["Empty"] * len(a) + a
        for i in range(len(tree) - 1, 1, -2):
            tree[i // 2] = max(tree[i], tree[i - 1])
        return tree



    def maxRange(self, tree, l, r, cd):
        left = len(tree) // 2 + l + cd
        right = len(tree) // 2 + r + cd
        ans = -10 ** 5
        while left <= right:
            if left % 2 != 0:
                ans = max(tree[left], ans)
            if right % 2 == 0:
                ans = max(tree[right], ans)
            
            left = (left + 1) // 2
            right = (right - 1) // 2
        return ans
