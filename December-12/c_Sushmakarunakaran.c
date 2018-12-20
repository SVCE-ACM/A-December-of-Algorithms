#include<stdio.h>
#include<stdlib.h>
typedef struct list
{
	int data;
	struct list *prev;
}node;

void main()
{
	struct list *head=NULL,*temp;
	int  i,n;
	printf("\n enter the number of entries");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{   node *p;
		p=(node*)malloc(sizeof(node));
		printf("\n enter the data");
		scanf("%d",&p->data);
		p->prev=NULL;
		if(head==NULL)
		  head=p;
		else
		{
			temp=head;
			p->prev=temp;
			head=p;
			
		  }  
		
	}
	printf("\n  the reversed input ");
	for(temp=head;temp!=NULL;temp=temp->prev)
	  printf("\n %d",temp->data);
	  
}
