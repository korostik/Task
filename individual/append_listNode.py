def append(node, value):
    new_node = ListNode()
    new_node.next = None
    new_node.val = value

    if node is None:
        return new_node
    temp = node
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node
    return node
