# АВЛ дерево
# Данное вращение используется тогда, когда разница высот R-поддерева и b-поддерева равна 2 и высота c-поддерева > высота L.
# class Node:
#     def __init__(self, value):
#         self.right = None
#         self.left = None
#         self.val = value



def Big_Right_Rotation(tree): # текущий узел основного дерева, который подходит под условие балансировки большим правым вращением
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




    

# tree = Node("a")
# tree.left = Node("b")
# tree.right = Node("R")
# tree.left.left = Node("L")
# tree.left.right = Node("c")
# tree.left.right.right = Node("N")
# tree.left.right.left = Node("M")
# tree = Big_Right_Rotation(tree)