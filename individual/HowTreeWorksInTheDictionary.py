class Dictionary:
    def __init__(self, key, value):
        self.right = None
        self.left = None
        self.key = key
        self.value = value

    def Add_and_Count(tree, key_new):
        temp = tree
        if tree == None:
            return Dictionary(key_new, 1)
        while True:
            if key_new > temp.key:
                if temp.right:
                    temp = temp.right
                else:
                    break
            else:
                if temp.left:
                    temp = temp.left
                else:
                    break

        if key_new > temp.key:
            temp.right = Dictionary(key_new, 1)
        elif key_new < temp.key:
            temp.left = Dictionary(key_new, 1)
        else:
            temp.value += 1
        return tree

    def get(tree, key_):
        temp = tree
        while temp:
            if temp.key < key_:
                temp = temp.right
            elif temp.key > key_:
                temp = temp.left
            else:
                return temp.value
        return None


# n = int(input())
# tree = None
# obj = Dictionary
# a = []
# for i in range(n):
#     print(a)
#     x, y = map(int, input().split())
#     a.append(x)
#     tree = obj.Add_and_Count(tree, x)
#     print(obj.get(tree, y))