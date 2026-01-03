# В онлайн-игре ведется таблица рейтинга игроков. Каждому игроку начисляются очки. Необходимо реализовать систему, которая должна обрабатывать три типа запросов:
# 1.  Добавить нового игрока с его рейтингом (или обновить рейтинг существующего игрока).
# 2.  Удалить игрока из таблицы.
# 3.  Найти место (ранг) игрока в таблице рейтинга. Место 1 — у игрока с наивысшим рейтингом.



class Tree:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value
    
def Add(tree, value_new):
    temp = tree
    if tree == None:
        return Tree(value_new)
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
        temp.right = Tree(value_new)
    else:
        temp.left = Tree(value_new)
    return tree
    
def find_root_minelement_in_right_tree(temp):
    ans = temp
    pred = None
    while temp:
        if temp.left:
            pred = temp
            ans = temp.left
            temp = temp.left
        else:
            temp = temp.right
    return ans, pred

def delete(tree, value):
    #удалять корень эта функция не может
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
                napr = temp_before_val.left
            else:
                napr = temp_before_val.right
            break
        
    #napr указывает на удаляемый элемент

    # удаление листа
    if napr.left == None and napr.right == None:
        if temp_before_val.left == napr:
            temp_before_val.left = None
        else:
            temp_before_val.right = None
    
    # удаление узла с одним ребенком
    if napr.left == None and napr.right != None or napr.left != None and napr.right == None:
        if temp_before_val.left == napr:
            if napr.left != None:
                temp_before_val.left = napr.left
            else:
                temp_before_val.left = napr.right
        else:
            if napr.left != None:
                temp_before_val.right = napr.left
            else:
                temp_before_val.right = napr.right
    
    # удаление узла с двумя детьми
    if napr.left != None and napr.right != None:
        minelement_in_right_tree, pred = find_root_minelement_in_right_tree(napr.right)
        napr.val = minelement_in_right_tree.val
        if pred == None: #нет самого левого элемента в правом дереве
            napr.val = minelement_in_right_tree.val
            napr.right = napr.right.right
        elif pred.left.right != None:
            pred.left = pred.left.right

tree = Tree(9)
tree.left = Tree(3)
tree.right = Tree(10)

tree.left.left = Tree(1)
tree.left.right = Tree(7)

tree.left.right.left = Tree(5)
tree.left.right.right = Tree(8)

tree.left.right.left.left = Tree(6)

delete(tree, 5)
print(tree.left.right.left.val)
