// https://leetcode.com/problems/insertion-sort-list/?envType=problem-list-v2&envId=linked-list


class Solution {
public:
    int len;
    ListNode* insertionSortList(ListNode* &node) {
        len = len_f(node);
        if (len <= 1){
            return node;
        }
        for (int i = 0; i < 2 * len; i++) {
            ListNode* temp = node;
            if (temp->val > temp->next->val) {
                node = replace_elements(temp, node, 0);
            }else{
                while (temp->next->next != nullptr) {
                    if (temp->next->val > temp->next->next->val) {
                        node = replace_elements(temp, node, -1);
                    }
                    temp = temp->next;
                }
            }
        }
        return node;
    }
private:
    ListNode* replace_elements(ListNode* temp, ListNode* &node, int k) {
        if (k == -1) {
            ListNode* per = temp->next;
            temp->next = temp->next->next;
            ListNode* pocl = temp->next->next;
            per->next = nullptr;
            temp->next->next = per;
            temp->next->next->next = pocl;
            return node;
        }
        ListNode* third = temp->next->next;
        ListNode* second = temp->next;
        temp->next = nullptr;
        ListNode* ans = nullptr;
        ans = append(ans, second->val);
        ans = append(ans, temp->val);
        ans->next->next = third;
        return ans;
    }
    int len_f(ListNode* node) {
        ListNode* temp = node;
        int len = 0;
        while (temp != nullptr){
            len += 1;
            temp = temp->next;
        }
        return len;
    }
    ListNode* append(ListNode* node, int value) {
        ListNode* new_node = new ListNode(value);

        if (node == nullptr) {
            return new_node;
        }
        ListNode* temp = node;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = new_node;
        return node;
    }
};
