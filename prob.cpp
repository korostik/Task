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
        while (node->next != nullptr){
            node = node->next;
        }
        node->next = Newnode;

    }
    return node;
    delete Newnode;
}

int main() {
    int length, value;
    s_node *node = nullptr;
    cin >> length;
    for(int i = 0; i < length; i++){
        cin >> value;
        node = append(node, value);
    }
    while (node != nullptr){
        cout << node->value << endl;
        node = node->next;
    }

    return 0;
}

//g++ prob.cpp && ./a.out