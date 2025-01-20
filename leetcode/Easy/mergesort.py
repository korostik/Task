# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = []
        ind1 = 0
        ind2 = 0
        for i in range(len(list1) + len(list2)):
            k = min(list1[ind1], list2[ind2])
            ans.append(k)
            if k == list1:
                ind1 += 1
            else:
                ind2 += 1
        return ans
        

        