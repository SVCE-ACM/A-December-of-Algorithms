#include<stdio.h>
void pascal(int);
int a[20][20];
int main()
{
	int i,j,n;
	printf("Enter the no. of rows ");
	scanf("%d",&n);
	pascal(n+1);
	return 0;
}
void pascal(int n)
{
	int i;
	if(n==1)
	{
		a[0][0]=1;
		printf("\nrow 0 --> 1");
		return;
	}
	else
	{
		pascal(n-1);
		a[n-1][0]=1;
		printf("\nrow %d --> %d\t",n-1,a[n-1][0]);
		for(i=1;i<n-1;i++)
		{
			a[n-1][i]=a[n-2][i-1]+a[n-2][i];
			printf("%d\t",a[n-1][i]);
		}
		a[n-1][n-1]=1;
		printf("%d",a[n-1][n-1]);
		return;
	}
}
