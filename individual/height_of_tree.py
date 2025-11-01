count = 0
height = 0
def h(tree):
    global count
    global ans
    if tree:
        count += 1
        height = max(height, count)
        h(tree.left)
        h(tree.right)
        count -= 1
