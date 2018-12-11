#include<stdio.h> 
#include<stdlib.h> 

struct Node 
{ 
	int data; 
	struct Node* next; 
}; 
void reverse(struct Node** head) 
{ 
    struct Node* first; 
    struct Node* rest; 
    if (*head == NULL) 
       return;    
    first = *head;   
    rest  = first->next; 
    if (rest == NULL) 
       return;    
    recursiveReverse(&rest); 
    first->next->next  = first;   
    first->next  = NULL;           
    *head = rest;               
}
struct Node* push(struct Node* head, int new_data) 
{ 
	struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));		 
	new_node->data = new_data; 
	new_node->next = head;	 
	head = new_node; 
    return head;
} 
// NOTE : Insertion from front of LIST. 
void printList(struct Node *head) 
{ 
	struct Node *temp = head; 
	while(temp != NULL) 
	{ 
		printf("%d\t", temp->data);	 
		temp = temp->next; 
	} 
    printf("\n");
}	 
int main() 
{
	struct Node* head = NULL; 
    int ch; 
    int y=1;

    do{

        printf("Enter choice : 1. Push 2. Reverse 3. PrintList: ");
        scanf("%d", &ch);
        if(ch==1)
            {
                printf("Enter value to insert : "); int n; scanf("%d",&n);
                head = push(head,n); 
            }
        else if(ch==2)
        {
            reverse(&head);
        }
        else
            printList(head);
        printf("Do you want to continue? 1/0  "); 
        scanf("%d",&y);

    }while(y==1);
    return 0;
	
} 
