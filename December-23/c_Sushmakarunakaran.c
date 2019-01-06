#include<stdio.h>
#include<string.h>
int main()
{
	int i,k=0,j,d,s,r,l,cl,n[10],b=0,m=1;
	char c[10][4];
	printf("Number of classrooms: ");
	scanf("%d",&cl);
	printf("Size of classrooms (r*c): ");
	scanf("%d%d",&r,&l);
	printf("Enter the number of departments (2-10): ");
	scanf("%d",&d);
	for(i=0;i<d;i++)
	{
		printf("Department %d Code: ",i+1);
		scanf("%s",c[i]);
	}
	for(i=0;i<d;i++)
	{
		printf("Students in department %d (1-100): ",i+1);
		scanf("%d",&n[i]);
	}
	m=1;
	for(i=0;i<r*cl;i++)
	{
		if(i%r==0)
		printf("\nRoom %d",++b);
		printf("\n");
		for(j=0;j<l;j++)
		{
			if(m>n[k])
			printf("_ _ \t");
			else
			printf("%s%d\t",c[k],m);
			k=(k+1)%d;
			if((j+1)%d==0)
			m++;
		}
		if(l%d==0)
		k=(k+d-1)%d;
	}
	return 0;
}

