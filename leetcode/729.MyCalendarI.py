# https://leetcode.com/problems/my-calendar-i/?envType=problem-list-v2&envId=segment-tree


tree = None
class Node:
    def __init__(self, a):
        self.right = None
        self.left = None
        self.val = a


class MyCalendar:

    def __init__(self):
        self.ans = []
        global tree
        tree = None

    def book(self, start: int, end: int) -> bool:
        global tree
        if tree is None:
            tree = Node([start, end])
            return True
        temp = tree
        while temp:
            if start >= temp.val[1]:
                if temp.right is None:
                    temp.right = Node([start, end])
                    return True
                temp = temp.right
            elif end <= temp.val[0]:
                if temp.left is None:
                    temp.left = Node([start, end])
                    return True
                temp = temp.left
            else:
                return False
