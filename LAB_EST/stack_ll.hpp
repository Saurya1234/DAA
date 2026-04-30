#ifndef STACK_LL_HPP
#define STACK_LL_HPP

#include <iostream>
#include <stdexcept>

template <typename T>
class Stack {
// time complexity:
//   push()  - O(1)
//   pop()   - O(1)
//   peek()  - O(1)
//   empty() - O(1)
//   size()  - O(n)
// space complexity:
//   O(n) total for the stack storage, O(1) auxiliary per operation
    struct Node {
        T data;
        Node* next;
        Node(T value) : data(value), next(nullptr) {}
    };

    Node* top;

public:
    Stack() : top(nullptr) {}

    ~Stack() {
        while (!empty()) {
            pop();
        }
    }

    void push(T value) {
        Node* newNode = new Node(value); 
        newNode->next = top;
        top = newNode;
    }

    void pop() {
        if (empty()) {
            throw std::underflow_error("Stack is empty!");
        }
        Node* temp = top;
        top = top->next;
        delete temp;
    }

    T peek() const {
        if (empty()) {
            throw std::underflow_error("Stack is empty!");
        }
        return top->data;
    }

    bool empty() const {
        return top == nullptr;
    }

    int size() const {
        int count = 0;
        Node* current = top;
        while (current) {
            count++;
            current = current->next;
        }
        return count;
    }
};

#endif
