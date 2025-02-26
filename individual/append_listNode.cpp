ListNode* append(ListNode *node, int value){

    ListNode* Newnode = new ListNode;
    Newnode->val = value;
    Newnode->next = nullptr;
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
