#include<stdio.h>



void ex1(int a[4][4],int n)
{
	int i,j,temp;
		for(j=0;j<n;j++)
	{
	
		temp=a[j][0];
		a[j][0]=a[j][3];
		a[j][3]=temp;
		
	}
	
	printf("\n \n");
	
for(i=0;i<n;i++)
		{
		printf("\n");
	for(j=0;j<n;j++)
	{
	
printf("\t%d",a[i][j]);
}
}

for(j=0;j<n;j++)
	{
	
		temp=a[0][j];
		a[0][j]=a[3][j];
		a[3][j]=temp;
		
	}
	
	printf("\n \n");
	
for(i=0;i<n;i++)
		{
		printf("\n");
	for(j=0;j<n;j++)
	{
	
printf("\t%d",a[i][j]);
}
}
	
}

void ex2(int a[4][4],int n)
{
	
	int i,j,temp;
		for(j=0;j<n;j++)
	{
	
		temp=a[j][0];
		a[j][0]=a[j][3];
		a[j][3]=temp;
		
	}
	
	printf("\n \n");
	
for(i=0;i<n;i++)
		{
		printf("\n");
	for(j=0;j<n;j++)
	{
	
printf("\t%d",a[i][j]);
}
}

/*for(j=0;j<n;j++)
	{
	
		temp=a[j][0];
		a[j][0]=a[j][3];
		a[j][3]=temp;
		
	}
	
	printf("\n \n");
	
for(i=0;i<n;i++)
		{
		printf("\n");
	for(j=0;j<n;j++)
	{
	
printf("\t%d",a[i][j]);
}
}*/
	
}

int main()
{
	int a[4][4];
	int n,m=0,i,j;
	
	int r=1,temp;
	
	printf("Enter the order:");
	scanf("%d",&n);
	m = n * (n*n+1)/2 ;
	printf("\nMagic sum =%d",m);
	
	for(i=0;i<n;i++)
	for(j=0;j<n;j++)
	
	{
		a[i][j]=r;
		r++;
	}
	
	/*for(i=0;i<n;i++)
		{
		printf("\n");
	for(j=0;j<n;j++)
	{
	
printf("\t%d",a[i][j]);
}
}*/

temp= a[0][0];
a[0][0]=a[3][3];
a[3][3]=temp;

temp= a[0][3];
a[0][3]=a[3][0];
a[3][0]=temp;

temp= a[1][1];
a[1][1]=a[2][2];
a[2][2]=temp;

temp= a[1][2];
a[1][2]=a[2][1];
a[2][1]=temp;

printf("\n \n");

	for(i=0;i<n;i++)
		{
		printf("\n");
	for(j=0;j<n;j++)
	{
	
printf("\t%d",a[i][j]);
}
}

ex1(a,n);

ex2(a,n);











	
	return 0;
}
