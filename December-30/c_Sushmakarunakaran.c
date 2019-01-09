#include<stdio.h>
void main ()
{
	int n;
	printf("\n \t enter the no. of sides");
	scanf("%d",&n);
	printf("\n \t No. of diagonals:%d",((n*(n-1))/2)-n);
}
