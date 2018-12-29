#include<stdio.h>
void main()
{
	int n;
	printf("\n \t enter the no. friends playing with tharun");
	scanf("%d",&n);
	n=n+1;
	printf("\n \t no. of strings required:%d",(n*(n-1))/2);
	
}
