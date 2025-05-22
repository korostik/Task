// https://leetcode.com/problems/add-two-numbers/?envType=problem-list-v2&envId=linked-list

ListNode* append(ListNode *node, int value) {
    ListNode* Newnode = new ListNode;
    Newnode->val = value;
    Newnode->next = nullptr;
    if (node == nullptr) {
        return Newnode;
    }
    ListNode* temp = node;
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = Newnode;

    return node;
}
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* node1, ListNode* node2) {
        ListNode* ans = nullptr;
        string s1 = "";
        ListNode * temp1 = node1;
        while (temp1 != nullptr) {
            s1 = to_string(temp1->val) + s1;
            temp1 = temp1->next;
        }
        
        ListNode* temp2 = node2;
        string s2 = "";
        while (temp2 != nullptr) {
            s2 = to_string(temp2->val) + s2;
            temp2 = temp2->next;
        }
        
        double x = stod(s1)+ stod(s2);
        string a = to_string(x);
        string s = "";
        for (auto i : a){
            if (isdigit(i)){
                s += i;
            }else{
                break;
            }
        }
        for (int i = s.length() - 1; i >= 0; i--){
            ans =append(ans, s[i] - '0');
        }
        return ans;
    }
};