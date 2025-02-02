class Solution(object):
    def twoSum(self, a, x):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] + a[j] == x:
                    return [i, j]

                    