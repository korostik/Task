class Solution:
    def removeDuplicates(self, nums):
        OK = True
        i = 0
        while OK:
            k = len(nums)
            nums = self.remove_1(nums, i)
            if i == len(nums) - 1:
                OK = False
            i += 1

        return len(nums)

    def remove_1(self, nums, i):
        while nums[i] in nums and nums.count(nums[i]) > 1:
            nums.remove(nums[i])
        return nums
