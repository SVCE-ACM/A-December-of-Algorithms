#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
typedef struct list
{
	int data;
	list *next;
}node;
node *temp,*temp1,*head=NULL,*temp2;
int main()
{
	int n,i;
	printf("Enter the no. of elements in the list: ");
	scanf("%d",&n);
	printf("\nEnter the elements: ");
	for(i=0;i<n;i++)
	{
		node *p;
		p=(node*)malloc(sizeof(node));
		scanf("%d",&p->data);
		p->next=NULL;
		if(head==NULL)
		head=p;
		else
		{
			temp=head;
			while(temp->next!=NULL)
			temp=temp->next;
			temp->next=p;
		}
	}
	printf("The reversed linked list is: ");
	temp=head;
	temp2=temp->next;
	for(i=0;i<n-1;i++)
	{
	    temp1=temp;
		temp=temp2;
		temp2=temp->next;
		temp->next=temp1;	
    }
    head->next=NULL;
	head=temp;
	for(temp=head;temp!=NULL;temp=temp->next)
	printf("%d\t",temp->data);	
	return 0;
}
