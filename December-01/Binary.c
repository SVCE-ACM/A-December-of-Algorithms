                                      // (Binary search)
#include<stdio.h>
void main()
{
	int a[20],n,s,high,low,mid,i,c=0,d,e;
	do
	{
	
	printf("Enter the number of elements: ");
	scanf("%d",&n);
	printf("\n\t\t\t\tEnter elements in order");
	for(i=0;i<n;i++)
	{
		printf("\n Enter element %d:",i+1);
		scanf("%d",&a[i]);
	}		
	do
	{	
	printf("\nEnter the element to be searched:");
	scanf("%d",&s);
	low=0;
	high=n-1;	
	while(high>=low)
	{
	    mid=(low+high)/2;	    
	    if(s==a[mid])
	    {
	    printf("\nThe element is found @ pos=%d",mid+1);
	    c++;
	    break;
	}
	else if(s>a[mid])
    low=mid+1;
	else
	high=mid-1;
}
if(c==0)
printf("\n The element is not found : sorry guys");
	printf("\n\n\t\t\tDo you want to continue your search process (yes==1 or No == 0)");
	scanf("%d",&d);			
}while(d==1);
printf("\n\n\t\t\t\tDo you want to continue the whole process (yes==1 or NO == 0)");	
scanf("%d",&e);
}while(e==1);
}
									      
