#include<stdio.h>
int main()
{
	int n,a[10],s1=0,s2=0,i,d,size;
	printf("Enter the number");
	scanf("%d",&n);
	for(i=0;n>0;i++)
	{
		d=n%10;
		a[i]=d;
		n=n/10;
	}
	size=i;
	for(i=0;i<size/2;i++)
	s1+=a[i];
	for(i=size/2;i<size;i++)
	s2+=a[i];
	if(s1==s2)
	printf("The given no. is lucky");
	else 
	printf("The given no. is not lucky");
	return 0;
}
