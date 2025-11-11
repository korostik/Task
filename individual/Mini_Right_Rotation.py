# Данное вращение используется тогда, когда разница высот R-поддерева и b-поддерева равна 2 и высота С <= высота L.
# class Node:
#     def __init__(self, value):
#         self.right = None
#         self.left = None
#         self.val = value



def Rotation(tree): # текущий узел основного дерева, который подходит под условие балансировки правым вращением
    a_left = tree.left #b
    tree.left = None
    b_right = a_left.right
    a_left.right = None
    tree.left = b_right
    a_left.right = tree
    return a_left




    

# tree = Node("a")
# tree.left = Node("b")
# tree.right = Node("R")
# tree.left.right = Node("C")
# tree.left.left = Node("L")
# tree = Rotation(tree)
