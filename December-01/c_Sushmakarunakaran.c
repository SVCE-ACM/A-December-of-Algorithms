#include<stdio.h>
#include<conio.h>
void main()
{
	int a[25],first,last,mid,search,n,i,s;
	do
		{
		
	printf("enter the no of elements ");
	scanf("%d",&n);
	printf("enter sorted elements ");
	
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("enter the element to be searched");
	scanf("%d",&search);
	first=0;
	last=n-1;
	while(first<=last)
	{
		mid=(first+last)/2;
		if(search==a[mid])
		{
		  printf("the element is found at %d ",mid+1);
                  break;
		}
	    if(search<a[mid])
		{       printf("the value is too high ");
			last=mid-1;
		}
		if(search>a[mid])
		{       printf("the value is too low");
			first=mid+1;
		}
		
	}
	if(first>last)
	{
		printf("the element is not found in the given array");
	}
	printf("enter 1 to continue and 0 to end ");
	scanf("%d",&s);
	
}while(s>0);
}
