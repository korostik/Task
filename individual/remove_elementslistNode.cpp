//https://leetcode.com/problems/remove-linked-list-elements/solutions/902295/simple-recusrion/

class Solution {
public:
    ListNode* removeElements(ListNode* node, int val) {
        ListNode* temp = node;
        int k;

        while (temp != nullptr) {
            k = 0;
            if (temp->next != nullptr && temp->next->val == val){
                temp->next = temp->next->next;
            }else{
                temp = temp->next;
            }
        }
        if (node != nullptr)
            if (node->val == val)return node->next;
        return node;
        
    }
};
