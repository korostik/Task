// https://leetcode.com/problems/linked-list-cycle/
class Solution {
    public:
        bool hasCycle(ListNode *head) {
            ListNode* temp1 = head;
            ListNode* temp2 = head;
            while (temp1 != nullptr && temp2 != nullptr) {
                temp1 = temp1->next;
                temp2 = temp2->next;
                if (temp2 == nullptr){
                    return false;
                }
                temp2 = temp2->next;
                if (temp1 == temp2){
                    return true;
                }
            }
            return false;
        }
    };
