# https://leetcode.com/problems/range-sum-query-mutable/description/?envType=problem-list-v2&envId=segment-tree


class NumArray:
    def __init__(self, nums):
        self.len_nums = len(nums)
        k = len(nums)
        i = 0
        while 2 ** i < k:
            i += 1
        nums += (2 ** i - k) * [0]
        self.len_nums2 = len(nums)
        self.ind_nach = 2 ** i - k
        self.nums = nums
        self.tree = self.create_tree()

    def update(self, index, val):
        self.fix_tree(self.tree, index, val)
        return self.tree

    def sum_range(self, left, right):
        tree = self.tree
        left = len(tree) - self.len_nums2 + left
        right = len(tree) - self.len_nums2 + right
        ans = 0
        while left <= right:
            if left % 2 != 0:
                ans += tree[left]
            if right % 2 == 0:
                ans += tree[right]
            
            left = (left + 1) // 2
            right = (right - 1) // 2
        return ans

    def create_tree(self):
        tree = ["Empty"] * len(self.nums) + self.nums

        right = 2 * len(self.nums) - 1
        left = len(self.nums) - 1
        k = len(self.nums)
        while tree[1] == "Empty":
            k //= 2 
            for i in range(right, left + 1, -2):
                a = tree[i]
                b = tree[i - 1]
                tree[i // 2] = a + b

            right = left
            left -= k
        
        return tree

    def fix_tree(self, tree, index, val):
        element_ind = len(tree) - self.ind_nach - self.len_nums + index
        difference = val - tree[element_ind]
        tek = element_ind // 2
        tree[element_ind] = val
        while tek > 0:
            tree[tek] += difference
            tek //= 2
        return tree
