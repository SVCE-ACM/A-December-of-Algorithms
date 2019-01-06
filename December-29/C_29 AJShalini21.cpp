#include<stdio.h>
int main()
{
	int n,s;
	printf("Enter the no. of friends ");
	scanf("%d",&n);
	s=n*(n-1)/2;
	printf("The no. of strings needed is %d",s);
	return 0;
}
