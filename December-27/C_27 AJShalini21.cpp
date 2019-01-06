#include<stdio.h>
int vow(char);
int main()
{
	int i,j,n,flag=0;
	char a[10][10];
	printf("Enter no. of strings ");
	scanf("%d",&n);
	printf("Enter the strings ");
	for(i=0;i<n;i++)
	scanf("%s",a[i]);
	for(i=0;i<n-1;i++)
	{
		j=0;
	    while(a[i][j+1]!='\0')
		{
			if(vow(a[i][j])==1&&vow(a[i+1][j])==1&&vow(a[i][j+1])==1&&vow(a[i+1][j+1])==1)
			{
				printf("\n%d - %d",i,j);
				flag++;
			}
			j++;
		}
	}
	if(flag==0)
	printf("\nUnavailable");
	return 0;
}
int vow(char c)
{
	if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
	return 1;
	else 
	return 0;
}
