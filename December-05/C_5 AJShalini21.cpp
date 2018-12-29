#include<stdio.h>
int i=1;
void tower(int,char[],char[],char[]);
int main()
{
	int n;
	char rod1[]="left",rod2[]="middle",rod3[]="right";
	printf("Enter the number of disks  ");
	scanf("%d",&n);
	tower(n,rod1,rod3,rod2);
	return 0;
}
void tower(int n,char rod1[],char rod3[],char rod2[])
{
	if(n==1)
	{
		printf("\n%d. %s => %s",i++,rod1,rod3);
		return;
	}
	tower(n-1,rod1,rod2,rod3);
	printf("\n%d. %s => %s",i++,rod1,rod3);
	tower(n-1,rod2,rod3,rod1);
}
