#include<stdio.h>
#include<string.h>

void rev(char *b)
{	
	if( *b)
	{
	
		rev(b+1);
		printf("%c",*b);
	
	}	
	
}

void main()
{
	char a[20];
	printf("Enter the string:");
	scanf("%s",a);
	rev(a);
}
