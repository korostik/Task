ListNode* remove_element(ListNode* & node, int val){
    ListNode* temp = node;
    while (temp != nullptr) {
        if (temp->next != nullptr){
            if (temp->next->val == val){
                temp->next = temp->next->next;
            }
        }
        temp = temp->next;
    }
    return node;
}