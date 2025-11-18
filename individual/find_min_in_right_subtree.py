class Node:
    def __init__(self, value=10**6):
        self.right = None
        self.left = None
        self.val = value

def Add(tree, value_new):
    temp = tree
    if tree == None:
        return Node(value_new)
    while True:
        if value_new > temp.val:
            if temp.right:
                temp = temp.right
            else:
                break
        else:
            if temp.left:
                temp = temp.left
            else:
                break
    if value_new > temp.val:
        temp.right = Node(value_new)
    else:
        temp.left = Node(value_new)
    return tree
temp = Node()
def f(tree):
    global temp
    if tree:
        k1 = tree.val
        k2 = temp.val
        if k1 < k2:
            temp = tree
        f(tree.left)
        f(tree.right)


tree = Node(6)
tree = Add(tree, 3)
tree = Add(tree, 5)
tree = Add(tree, 8)
tree = Add(tree, 7)
tree = Add(tree, 9)
tree = Add(tree, 2)
tree = Add(tree, 4)
tree = Add(tree, 1)
tree = Add(tree, 10)
tree = Add(tree, 11)
tree = Add(tree, 0)
f(tree.right)
print(temp.val)