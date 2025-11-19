# АВЛ дерево
# Данное вращение используется тогда, когда разница высот L-поддерева и b-поддерева равна 2 и высота С <= высота R.
# class Node:
#     def __init__(self, value):
#         self.right = None
#         self.left = None
#         self.val = value




def Mini_Left_Rotation(tree): # текущий узел основного дерева, который подходит под условие балансировки малым левым вращением
    b_left = tree.right.left
    tree.right.left = None
    a_right = tree.right
    tree.right = None
    tree.right = b_left
    a_right.left = tree
    return a_right

    

# tree = Node("a")
# tree.left = Node("L")
# tree.right = Node("b")
# tree.right.left = Node("C")
# tree.right.right = Node("R")
# tree = Mini_Left_Rotation(tree)
