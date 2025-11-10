# Данное вращение используется тогда, когда разница высот R-поддерева и b-поддерева равна 2 и высота c-поддерева > высота L.
class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value



def Rotation(tree): # текущий узел основного дерева, который подходит под условие балансировки
    c_ = tree.left.right
    m_ = c_.left
    n_ = c_.right
    tree.left.right = None
    b_ = tree.left
    b_.right = m_
    tree.left = None
    tree.left = n_
    c_.right = tree
    c_.left = b_
    return c_




    

tree = Node("a")
tree.left = Node("b")
tree.right = Node("R")
tree.left.left = Node("L")
tree.left.right = Node("c")
tree.left.right.right = Node("N")
tree.left.right.left = Node("M")
tree = Rotation(tree)
print(tree.val)
print(tree.left.val)
print(tree.right.val)
print(tree.left.left.val)
print(tree.left.right.val)
print(tree.right.left.val)
print(tree.right.right.val)