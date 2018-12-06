#include<stdio.h>
int gcd(int x,int y)
{ 
	if(y==0)
	 return x;
	 else	
	 gcd(y,x%y);
}
void main()
{
	int x,g=0,y,temp,l;
	printf("Enter the two numbers :");
	scanf("%d %d",&x,&y);
	temp=(x*y);
	g=gcd(x,y);
	l=(temp)/g;	
	printf("\n\n\t\t\tLcm=%d",l);
}

