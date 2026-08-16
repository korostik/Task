ListNode* append_ListNode(ListNode* node, ListNode* Newnode){
    if (Newnode = nullptr){
        return node;
    }
    ListNode* temp = node;
    while (temp->next != nullptr){
        temp = temp->next;
    }
    temp->next = Newnode;
    return node;
}
