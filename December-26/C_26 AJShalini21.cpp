#include<stdio.h>
int main()
{
	int n,i,j=0,flag=0;
	char a[10][20];
	printf("Enter the no. of strings ");
	scanf("%d",&n);
	printf("Enter the strings ");
	for(i=0;i<n;i++)
	scanf("%s",&a[i]);
	do
	{
	    for(i=0;i<n-1;i++)
	    {
		    if(a[i][j]==a[i+1][j])
		    continue;
		    else
		    {
		    	flag++;
		    	break;
			}   
	    }
	    if(flag!=0)
	    break;
	    j++;
    }while(a[0][j]!='\0');
	if(j<=1)
	printf("No common prefix");
	else
	{
	    printf("Common prefix is ");
		for(i=0;i<j;i++)
		printf("%c",a[0][i]);	
	}
	return 0;
}
