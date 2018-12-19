#include <bits/stdc++.h>
using namespace std;

//node definition
struct Node {
    int data;
    Node* next;
};

//global head.
Node* head = NULL;   //empty list.

/**
  * @desc: function to create a node with two fields (as a Node def).
  * @param: data for the Node.
  * @return: the newNode.
  */
Node* create_New_Node(int data) {

    Node* newNode = new Node();     //creating and allocating the memory for new Node.

    newNode -> data = data;         //assigning the data to the data field of the new Node.
    newNode -> next = NULL;

    return newNode;
}

/**
  * @desc: function to insert the data at the end of the linked list.
  * @param: data to be inserted.
  */
void InsertAtEnd(int data) {

    Node* newNode = create_New_Node(data);

    //if the LIST is empty.
    if( head == NULL) {
        head = newNode;
        return;
    }

    //if the LIST has at least one Node.
    Node* temp = head;

    //traversing till the last Node.
    while(temp -> next != NULL ) {
        temp = temp -> next;
    }

    temp -> next = newNode;

}

/**
  * @desc: function to print the elements of the LIST.
  */
void printList() {

    //if the LIST is empty.
    if(head == NULL) {
        cout << "LIST is empty, nothing to print..." << endl;
        return;
    }

    //if the LIST is not empty.
    Node* temp = head;

    cout << endl << "The List is... ";
    while(temp != NULL) {
        cout << temp -> data << " -> ";
        temp = temp -> next;
    }
    cout << "NULL" << endl;

}

/**
  * @desc: iterative function that reverses the linked list.(in-place)
  */
void reverseList() {

    Node *previousNode = NULL, *currentNode = head, *nextNode;

    while(currentNode != NULL) {
        nextNode = currentNode -> next;
        currentNode -> next = previousNode;
        previousNode = currentNode;
        currentNode = nextNode;
    }
    head = previousNode;
}

int main() {

    //10 -> 20 -> 34 -> 23 -> 889
    InsertAtEnd(10);
    InsertAtEnd(20);
    InsertAtEnd(34);
    InsertAtEnd(23);
    InsertAtEnd(889);

    printList();      //before reversing

    reverseList();    //reversing the List

    printList();      //after reversing
}


/*
Output:

    The List is... 10 -> 20 -> 34 -> 23 -> 889 -> NULL

    The List is... 889 -> 23 -> 34 -> 20 -> 10 -> NULL

*/
