// https://leetcode.com/problems/reorder-list/?envType=problem-list-v2&envId=linked-list

class Solution {
public:
    int main_len;
    void reorderList(ListNode* & node) {
        if (node == nullptr) {
            return;
        }
        main_len = len_f(node);
        int count;
        ListNode* main_temp = node;
        while (main_temp && main_temp->next && main_temp->next->next) {
            ListNode* temp = node;
            count = 1;
            while (count != main_len - 1 && temp) {
                temp = temp->next;
                count++;
            }
            node = replace_elements(main_temp, temp, node);

            main_temp = main_temp->next->next;
        }
    }
    
private:
    int len_f(ListNode* node) {
        ListNode* temp = node;
        int len = 0;
        while (temp) {
            len += 1;
            temp = temp->next;
        }
        return len;
    }

    ListNode* replace_elements(ListNode* temp1, ListNode* temp2, ListNode* &node) {
        if (temp1 == nullptr || temp2 == nullptr) {
            return node;
        }
        ListNode* first = temp2->next;
        temp2->next = nullptr;
        first->next = temp1->next;
        temp1->next = first;
        return node;
    }
};
