#  https://leetcode.com/problems/add-two-numbers/?envType=problem-list-v2&envId=linked-list

def ad(node, value):
    new_node = ListNode()
    new_node.val = value
    new_node.next = None
    if node is None:
        return new_node
    temp = node
    while temp.next != None:
        temp = temp.next
    temp.next = new_node
    return node

class Solution:
    def addTwoNumbers(self, node1, node2):
        num1 = 0
        p1 = 0
        temp1 = node1
        while temp1 != None:
            num1 += temp1.val * (10 ** p1)
            p1 += 1
            temp1 = temp1.next
        
        num2 = 0
        p2 = 0
        temp2 = node2
        while temp2 != None:
            num2 += temp2.val * (10 ** p2)
            p2 += 1
            temp2 = temp2.next
        x = num1 + num2
        listi = list(map(int, str(x).replace("", " ").split()))[::-1]
        ans = None
        for i in range(len(listi)):
            ans = ad(ans, listi[i])
        return ans