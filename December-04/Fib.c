#include<stdio.h>

void main()
{
	int n,sum=0,temp1,temp2,i;
	printf("Enter the limit untill you need to find the series:");
	scanf("%d",&n);
	printf("\n0\t1");
	temp2=1;
	temp1=0;
	for(i=2;i<n;i++)
	{
	   sum=temp2+temp1;
		printf("\t%d",sum);
		temp1=temp2;
		temp2=sum;
				
	}
	
}
