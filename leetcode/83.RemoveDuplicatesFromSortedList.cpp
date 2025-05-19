//https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?difficulty=EASY&page=1
ListNode* append(ListNode *node, int value){

    ListNode* Newnode = new ListNode;
    Newnode->val = value;
    Newnode->next = nullptr;
    if (node == nullptr){
        return Newnode;
    }else{
        ListNode* temp = node;
        while (temp->next != nullptr){
            temp = temp->next;
        }
        temp->next = Newnode;

    }
    return node;
}


bool f(ListNode* ans, int value){
    ListNode* temp;
    temp = ans;
    while (temp != nullptr){
        if (temp->val == value){
            return false;
        }
        temp = temp->next;
    }
    return true;
}

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* node){
        ListNode* ans = nullptr;
        ListNode* temp;
        temp = node;
        while (temp != nullptr){
            if (f(ans, temp->val)){
                ans = append(ans, temp->val);
            }
            temp = temp->next;
        }
        return ans;
    }
};
