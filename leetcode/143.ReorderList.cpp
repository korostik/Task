// https://leetcode.com/problems/reorder-list/description/?envType=problem-list-v2&envId=linked-list

#include <iostream>
using namespace std;

class ListNode{
public:
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

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



class Solution{
public:
    int main_len;
    void reorderList(ListNode* & node) {
        main_len = len_f(node);
        int count;
        ListNode* main_temp = node;
        while (main_temp->next->next != nullptr){
            ListNode* temp = node;
            count = 1;
            while (count != main_len - 1){
                temp = temp->next;
                count++;
            }
            ListNode* last = temp->next;
            temp->next->next = nullptr;
            last->next = main_temp->next;
            main_temp->next = last;


            main_len--;
            main_temp = main_temp->next->next;
        }
    }
    
    int len_f(ListNode* node){
        ListNode* temp = node;
        int len = 0;
        while (temp != nullptr){
            len += 1;
            temp = temp->next;
        }
        return len;
    }
};


int main(){
    Solution obj;
    ListNode* node = nullptr;
    int n, x;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> x;
        node = append(node, x);
    }
    obj.reorderList(node);
    ListNode* temp = node;
    while (temp != nullptr){
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout << endl;
}
// g++ 143.ReorderList.cpp && ./a.out

