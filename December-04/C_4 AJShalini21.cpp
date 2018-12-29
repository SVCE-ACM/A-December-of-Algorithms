#include<stdio.h>
int main()
{
	int pv=0,cv=1,nv=0,n,i;
	printf("Enter the value of n ");
	scanf("%d",&n);
	for(i=3;i<=n;i++)
	{
		nv=cv+pv;
		pv=cv;
		cv=nv;
	}
	if(n==1||n==2)
	printf("The %dth fibonacci no. is %d",n,n-1);
	else
	printf("The %dth fibonacci no. is %d",n,nv);
	return 0;
}
