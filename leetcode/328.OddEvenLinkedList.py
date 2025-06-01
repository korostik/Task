# https://leetcode.com/problems/odd-even-linked-list/?envType=problem-list-v2&envId=linked-list


def append(node, value):
    new_node = ListNode()
    new_node.next = None
    new_node.val = value

    if node is None:
        return new_node
    temp = node
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node
    return node
        





class Solution(object):
    def oddEvenList(self, node):
        if node == None:
            return node
        temp = node
        new_node = None
        while temp.next != None:
            value = temp.next.val
            new_node = append(new_node, value)
            if temp.next.next == None:
                temp.next = temp.next.next
                break
            temp.next = temp.next.next
            temp = temp.next
        temp.next = new_node
        return node
