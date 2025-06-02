ListNode* append(ListNode* &node, int value){
    
    ListNode* Newnode = new ListNode(value);
    if (Newnode == nullptr){
        cout << "Ошибка выделения памяти";
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