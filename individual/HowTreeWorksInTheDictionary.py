class Tree:
    def __init__(self, key, value=1):
        self.right = None
        self.left = None
        self.val = [key, value]

def Add_and_Count(tree, value_new):
    temp = tree
    if tree == None:
        return Tree(value_new)
    while True:
        if value_new > temp.val[0]:
            if temp.right:
                temp = temp.right
            else:
                break
        else:
            if temp.left:
                temp = temp.left
            else:
                break

    if value_new > temp.val[0]:
        temp.right = Tree(value_new)
    elif value_new < temp.val[0]:
        temp.left = Tree(value_new)
    else:
        temp.val[1] += 1
    return tree

def get(tree, value):
    temp = tree
    while temp:
        if temp.val[0] < value:
            temp = temp.right
        elif temp.val[0] > value:
            temp = temp.left
        else:
            return temp.val[1]
    return "ERROR"


# n = int(input())
# tree = None
# a = []
# for i in range(n):
#     print(a)
#     x, y = map(int, input().split())
#     a.append(x)
#     tree = Add_and_Count(tree, x)
#     print(get(tree, y))