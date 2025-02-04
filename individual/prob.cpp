#include <iostream>
using namespace std;

class s_node {
public:
    s_node *next;
    int value;
};

s_node* append(s_node *node, int value){

    s_node* Newnode = new s_node;
    Newnode->value = value;
    Newnode->next = nullptr;
    if (node == nullptr){
        return Newnode;
    }else{
        s_node* temp = node;
        while (temp->next != nullptr){
            temp = temp->next;
        }
        temp->next = Newnode;

    }
    return node;
}

int main() {
    int length, value;
    s_node *node = nullptr;
    cin >> length;
    for(int i = 0; i < length; i++){
        cin >> value;
        node = append(node, value);
    }
    
    s_node* temp;
    temp = node;
    while (temp != nullptr){
        cout << temp->value << endl;
        temp = temp->next;
    }

    return 0;
}

//g++ prob.cpp && ./a.out