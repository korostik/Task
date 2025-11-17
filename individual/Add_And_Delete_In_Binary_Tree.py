class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value
    
def Add(tree, value_new):
    temp = tree
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
    

def delete(tree, value):
    #найти то что удаляем
    temp = tree
    if temp.val != value:
        while True:
            k = temp.val
            if temp.right != None and value > temp.right.val:
                if temp.right:
                    temp = temp.right
                else:
                    break
            elif temp.left != None and value < temp.left.val:
                if temp.left:
                    temp = temp.left
                else:
                    break
            else:
                if temp.left and temp.left.val == value:
                    napr = 'left'
                else:
                    napr = 'right'
                break
    #если два ребенка Null, то делаем этот узел Null
    if napr == 'right':
        if temp.right.right == None and temp.right.left == None:
            temp.right = None
            return temp
    if napr == 'left':
        if temp.left.right == None and temp.left.left == None:
            temp.left = None
            return temp
    
    #если один ребенок Null, то передвигаем ребенка на место того, кого мы должны удалить
    if napr == 'right':
        if temp.right.right == None and temp.right.left != None:
            n = temp.right.left
            temp.right.left = None
            temp.right = n
            return temp
        if temp.right.right != None and temp.right.left == None:
            n = temp.right.right
            temp.right.right = None
            temp.right = n
            return temp
        
    if napr == 'left':
        if temp.left.right == None and temp.left.left != None:
            n = temp.left.left
            temp.left.left = None
            temp.left = n
            return temp
        
        if temp.left.right != None and temp.left.left == None:
            n = temp.left.right
            temp.left.right = None
            temp.left = n
            return temp
        
    #находим в правом дереве самый левый элемент и переставляем его ребенка(если он есть) на место родителя а родителя на место удаляемого элемента
    




tree = Node(6)
tree.left = Node(5)
tree.right = Node(7)
tree.left.right = Node(8)
tree = delete(tree, 5)
print(tree.left.val)