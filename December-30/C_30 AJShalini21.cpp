#include<stdio.h>
int main()
{
	int n,d;
	printf("Enter the no. of sides ");
	scanf("%d",&n);
	d=n*(n-3)/2;
	printf("The no. of diagonals is %d",d);
	return 0;
}
