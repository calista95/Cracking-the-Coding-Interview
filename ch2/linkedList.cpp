/*
Description: linked list implementation for Chapter 2 problems 
*/


#include <iostream>
using namespace std;

struct Node
{
    Node * next; //pointer to next node 
    int data; //holds the data 
}; 

class linkedList
{
    private:
    Node * head;
    Node * tail;
    int nodeCount;
    public:
    linkedList(); //constructor
    Node* createNew(int value); //creates a new node and returns a pointer to it 
    void addNode(int value); //adds a new node to the list 
    void printList(); //prints out the current list 
};


 linkedList::linkedList() //constructor
{ 
    head= NULL;
    tail=NULL;
    nodeCount=0;
};

Node* linkedList::createNew(int value)
{
    Node * newNode = new Node;
    newNode->data = value;
    newNode->next = NULL;
    nodeCount++; //increment count 
    if (head == NULL && tail == NULL){ //this means head is not pointing to anything yet (first time we are putting something in)
        head = newNode;
        tail = newNode;
    }

    return newNode;
}

void linkedList::addNode(int value) //function that creates a new node with the value specified 
{
 
    //create new node 
    Node * newNode = createNew(value);

    if (head != NULL && tail != NULL)
    {
        //attach it to the list 
        tail->next = newNode;
        tail = newNode;
    }
}

void linkedList::printList()
{
    Node * current = head; 
    for (int i=0; i<nodeCount; i++)
    {
        cout << "value: " << current->data << endl;
        current = current->next;
    }
}

int main()
{
    
    linkedList list;
    for (int i=0; i<3; i++)
    {
        list.addNode(i);
    }
    list.printList();

    return 0;
}