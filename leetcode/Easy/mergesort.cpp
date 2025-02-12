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

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* node1, ListNode* node2) {
        ListNode* ans = nullptr;

        int a, b, prov1 = 1, prov2 = 1;
        ListNode* temp1;
        temp1 = node1;
        ListNode* temp2;
        temp2 = node2;

        if (temp1 == nullptr){
            prov1 = 0;
        }else if(temp2 == nullptr){
            prov2 = 0;
        }


        while (temp1 != nullptr && temp2 != nullptr){
            a = temp1->val;
            b = temp2->val;
            if (a > b){
                ans = append(ans, b);
                temp2 = temp2->next;
            }else{
                ans = append(ans, a);
                temp1 = temp1->next;
            }
            
            if (temp1 == nullptr){
                prov1 = 0;
            }else if(temp2 == nullptr){
                prov2 = 0;
            }
        }

        if (prov1 == 0){
            while (temp2 != nullptr){
                ans = append(ans, temp2->val);
                temp2 = temp2->next;
            }
        }else if(prov2 == 0){
            while (temp1 != nullptr){
                ans = append(ans, temp1->val);
                temp1 = temp1->next;
            }
        }
        return ans;
    }
};


