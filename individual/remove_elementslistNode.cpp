class Solution {
public:
    ListNode* removeElements(ListNode* node, int val) {
        ListNode* temp = node;
        int k = 0;
        while (temp != nullptr) {
            if (temp->next != nullptr){
                if (temp->next->val == val){
                    temp->next = temp->next->next;
                    k = 1;
                }
            }
            if (k == 0){temp = temp->next;}
            else{k = 0;}    
        }
        if (node != nullptr){
            if (node->val == val){
                return node->next;
            }else{
                return  node;
            }
        }else{
            return node;
        }
        
    }
};