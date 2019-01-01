#include<stdio.h>
#include<string.h>

void main()
{
	char a[100], b[20][20];
	
	int l,i=0,k=0,j=0;
	
	printf("Enter the string:");
	gets(a);
	l=strlen(a);
	
	while(a[i]!='\0')
	{
		if(a[i] == ' ')
		{
			b[k][j]='\0';
			k++;
			j=0;
			
		}
		else
		{
			b[k][j]=a[i];
			j++;
			
			
		}
		b[k][j]='\0';
		
	i++;	
	}		
	
	for(i=0;i<=k;i++)
	for(j=i+1;j<=k;j++)
	{
		if(strcmp(b[i],b[j]) == 0)
		{
			printf("\n Word repeated: %s",b[i]);
		}
		
	}
	
}
