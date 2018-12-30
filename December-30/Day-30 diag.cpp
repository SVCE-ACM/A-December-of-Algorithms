#include<stdio.h>

int main()
{
	int n;
	
	printf("Enter the no. of sides in polygon:");
	scanf("%d",&n);
	printf("\n output : %d",(n*(n-3))/2);
	
	return 0;
}
