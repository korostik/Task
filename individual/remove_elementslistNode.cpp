class Solution {
public:
    ListNode* removeElements(ListNode* node, int val) {
        ListNode* temp = node;
        int k;
        
        while (temp != nullptr) {
            k = 0;
            if (temp->next != nullptr){
                if (temp->next->val == val){
                    temp->next = temp->next->next;
                    k = 1;
                }
            }
            if (k == 0){temp = temp->next;}
        }
        if (node != nullptr)
            if (node->val == val)return node->next;
        return node;
        
    }
};
