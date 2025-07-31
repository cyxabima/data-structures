#include <iostream>
using namespace std;

struct Node {
    int val;
    Node* next;
    Node(int val) {
        this->val = val;
        this->next = nullptr;
    }
};

class List {
public:
    List();
    void push(int val);
    int pop();

private:
    Node* head;
};

List::List() {
    this->head = nullptr;
}

void List::push(int val) {
    Node* new_node = new Node(val);
    if (this->head == nullptr) {
        this->head = new_node;
    } else {
        Node* last = head;
        while (last->next != nullptr) { // FIXED: != instead of ==
            last = last->next;
        }
        last->next = new_node;
    }
}

int List::pop() {
    if (this->head == nullptr) {
        throw runtime_error("Can't pop from empty list");
    }

    Node* last = head;
    Node* prev = nullptr;

    if (head->next == nullptr) {
        int val = head->val;
        delete head;
        head = nullptr;
        return val;
    }

    while (last->next != nullptr) { // FIXED: != instead of ==
        prev = last;
        last = last->next;
    }

    int val = last->val;
    prev->next = nullptr;
    delete last;
    return val;
}

int main() {
    List* list = new List();
    list->push(10);
    list->push(20);
    list->push(30);
    cout << (*list).pop() << endl;  // Outputs: 30
    cout << list->pop() << endl;  // Outputs: 20
    cout << list->pop() << endl;  // Outputs: 10
    delete list;
    return 0;
}
