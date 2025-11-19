count = 0
height = 0
def h(tree):
    global count
    global height
    if tree:
        count += 1
        height = max(height, count)
        h(tree.left)
        h(tree.right)
        count -= 1
#answer is the height
