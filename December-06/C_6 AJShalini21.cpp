#include<stdio.h>
int gcd(int,int);
int main()
{
	int a[10],n,lcm=1,i;
	printf("Enter no. of elements  ");
	scanf("%d",&n);
	printf("Enter the elements  ");
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(i=0;i<n;i++)
	{
	lcm=a[i]*lcm/gcd(a[i],lcm);
    }
	printf("Lcm is %d",lcm);
	return 0;
}
int gcd(int a,int b)
{
	while(a!=b)
	{
		if(a>b)
		return gcd(a-b,b);
		else
		return gcd(a,b-a);
	}
	return a;
}
