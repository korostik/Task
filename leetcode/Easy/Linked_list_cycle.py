/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        int c = 0;
        ListNode* temp = head;
        while (temp != nullptr && temp->next != nullptr) {
            c += 1;
            if (c > 110000) {
                return true;
            }
            temp = temp->next;
        }
        return false;
    }
};