# Данное вращение используется тогда, когда разница высот L-поддерева и b-поддерева равна 2 и высота c-поддерева > высота R.
# class Node:
#     def __init__(self, value):
#         self.right = None
#         self.left = None
#         self.val = value



def Rotation(tree): # текущий узел основного дерева, который подходит под условие балансировки
    new_tree = Node(tree.right.left.val)
    c_left = tree.right.left.left
    c_right = tree.right.left.right
    a_right = tree.right
    a_right.left = c_right
    new_tree.right = a_right
    tree.right = None
    tree.right = c_left
    new_tree.left = tree
    return new_tree




    

# tree = Node("a")
# tree.left = Node("L")
# tree.right = Node("b")
# tree.right.left = Node("c")
# tree.right.right = Node("R")
# tree.right.left.right = Node("N")
# tree.right.left.left = Node("M")
# tree = Rotation(tree)
