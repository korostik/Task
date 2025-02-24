class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        head = [1, 1, 2, 3, 4, 5, 6]
        ans = [0] * len(head)
        k = ""
        j = 0
        for i in range(len(head)):
            if k != head[i]:
                k = head[i]
                ans[j] = head[i] 
                j += 1
        print(ans[:j])

        