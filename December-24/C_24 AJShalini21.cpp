#include<stdio.h>
void reverse(char,int);
char a[20];
int main()
{
	printf("Enter String: ");
	gets(a);
	reverse(a[0],0);
	return 0;
}
void reverse(char c,int i)
{
    if(c=='\0')
     return;
    else
     reverse(a[i+1],i+1);
     printf("%c",c);
}
