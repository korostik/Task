ListNode* append(ListNode* &node, int value, bool& flag){
    
    ListNode* Newnode = new ListNode(value);
    if (Newnode == nullptr){
        flag = true;
        return node;
    }
    if (node == nullptr){
        return Newnode;
    }
    ListNode* temp = node;
    while (temp->next != nullptr){
        temp = temp->next;
    }
    temp->next = Newnode;

    return node;
}
