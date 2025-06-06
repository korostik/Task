ListNode* createnode(int value) {
    ListNode* Newnode = new ListNode();
    if (!Newnode) {
        return nullptr;
    }
    Newnode->val = value;
    newNode->next = nullptr;
    return Newnode;
}
