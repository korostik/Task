# АВЛ дерево
class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value


class Rotation:
    def Big_Left_Rotation(temp): # текущий узел основного дерева, который подходит под условие балансировки большим левым вращением
        # Данное вращение используется тогда, когда разница высот L-поддерева и b-поддерева равна 2 и высота c-поддерева > высота R.
        new_temp = Node(temp.right.left.val)
        c_left = temp.right.left.left
        c_right = temp.right.left.right
        a_right = temp.right
        a_right.left = c_right
        new_temp.right = a_right
        temp.right = None
        temp.right = c_left
        new_temp.left = temp
        return new_temp
    
    def Big_Right_Rotation(temp): # текущий узел основного дерева, который подходит под условие балансировки большим правым вращением
        # Данное вращение используется тогда, когда разница высот R-поддерева и b-поддерева равна 2 и высота c-поддерева > высота L.
        c_ = temp.left.right
        m_ = c_.left
        n_ = c_.right
        temp.left.right = None
        b_ = temp.left
        b_.right = m_
        temp.left = None
        temp.left = n_
        c_.right = temp
        c_.left = b_
        return c_
    
    def Mini_Left_Rotation(temp): # текущий узел основного дерева, который подходит под условие балансировки малым левым вращением
        # Данное вращение используется тогда, когда разница высот L-поддерева и b-поддерева равна 2 и высота С <= высота R.
        b_left = temp.right.left
        temp.right.left = None
        a_right = temp.right
        temp.right = None
        temp.right = b_left
        a_right.left = temp
        return a_right
    
    def Mini_Right_Rotation(temp): # текущий узел основного дерева, который подходит под условие балансировки малым правым вращением
        # Данное вращение используется тогда, когда разница высот R-поддерева и b-поддерева равна 2 и высота С <= высота L.
        a_left = temp.left #b
        temp.left = None
        b_right = a_left.right
        a_left.right = None
        temp.left = b_right
        a_left.right = temp
        return a_left
