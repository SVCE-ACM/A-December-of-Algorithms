#include<stdio.h>
#include<stdlib.h>

typedef struct list
{
	int data;
	struct list *next;
	
}node;

node *p,*temp,*head=NULL,*prev=NULL,*temp2;

void create()
{
	int n,i;
	printf("\n\nEnter the no. of digits in list:");
	scanf("%d",&n);
	
	for(i=0;i<n;i++)
	{
		p=(node *)malloc(sizeof(node));
		p->next=NULL;
		printf("\nEnter the %d digit:",i+1);
		scanf("%d",&p->data);
		if(head==NULL)
		head=p;
		else
		{
			temp=head;
			while(temp->next!=NULL)
			temp=temp->next;
			
			temp->next=p;
			p->next=NULL;
		}
	}
	
}

void disp()
{
	printf("\n");
	for(temp=head;temp!=NULL;temp=temp->next)
	{
		
		printf("\t%d",temp->data);
	}
}

void rev()
{
	temp = head;
	
	while(temp!=NULL)
	{
		temp2=temp->next;
		temp->next=prev;
		prev=temp;
		temp=temp2;
	
	}
	
	head = prev;

}

void main()
{
	int ch;
	do
	{

        printf("\n\n1.create linked list\n2.reverse it\n3.print it.....");
		printf("\n\nEnter your choice:");
		scanf("%d",&ch);
		
		switch (ch)
		{
			case 1:
				{
					create();
					break;
				}
			case 2:
			{
				rev();
				break;
				}
			case 3:
			{
				disp();
				break;
					}		
		}
	
	
}while(ch<=3);
}

