# В онлайн-игре ведется таблица рейтинга игроков. Каждому игроку начисляются очки. Необходимо реализовать систему, которая должна обрабатывать три типа запросов:
# 1.  Добавить нового игрока с его рейтингом (или обновить рейтинг существующего игрока).
# 2.  Удалить игрока из таблицы.
# 3.  Найти место (ранг) игрока в таблице рейтинга. Место 1 — у игрока с наивысшим рейтингом.



class Node:
    def __init__(self, value):
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
    

def delete(tree, value):
    #найти то что удаляем
    temp = tree
    while temp:
        if temp != None and value > temp.val:
            temp_before_val = temp
            temp = temp.right
        elif value < temp.val:
            temp_before_val = temp
            temp = temp.left
        else:
            if temp_before_val.left and temp_before_val.left.val == value:
                napr = 'left'
            else:
                napr = 'right'
            break
    
    
    #если два ребенка Null, то делаем этот узел Null
    if napr == 'right':
        if temp_before_val.right.right == None and temp_before_val.right.left == None:
            temp_before_val.right = None
            return tree
    if napr == 'left':
        if temp_before_val.left.right == None and temp_before_val.left.left == None:
            temp_before_val.left = None
            return tree
    
    #если один ребенок Null, то передвигаем ребенка на место того, кого мы должны удалить
    if napr == 'right':
        if temp_before_val.right.right == None and temp_before_val.right.left != None:
            n = temp_before_val.right.left
            temp_before_val.right.left = None
            temp_before_val.right = n
            return tree
        if temp_before_val.right.right != None and temp_before_val.right.left == None:
            n = temp_before_val.right.right
            temp_before_val.right.right = None
            temp_before_val.right = n
            return tree
        
    if napr == 'left':
        if temp_before_val.left.right == None and temp_before_val.left.left != None:
            n = temp_before_val.left.left
            temp_before_val.left.left = None
            temp_before_val.left = n
            return tree
        
        if temp_before_val.left.right != None and temp_before_val.left.left == None:
            n = temp_before_val.left.right
            temp_before_val.left.right = None
            temp_before_val.left = n
            return tree
        
    #находим в правом дереве самый левый элемент и переставляем его ребенка(если он есть) на место родителя а родителя на место удаляемого элемента
    

