#include<stdio.h>
int vowel(char a)
{
	if(a =='a'||a =='e'||a =='i'||a =='o'||a =='u'||a =='A'||a =='E'||a =='I'||a =='O'||a =='U')
	 return 1;
	else
	 return 0; 
}
int main ()
{
	char a[10][10];
	int i,j,r,c;
	printf("\n enter the no. of rows and columns");
	scanf("%d%d",&r,&c);
	printf("\n enter the strings");
		for(i=0;i<r;i++)
	{     scanf("%s",a[i]);
    }

	for(i=0;i<r;i++)
	{  
		for(j=0;j<c;j++)
		{   
			if(vowel(a[i][j])==1&&vowel(a[i][j+1])==1&&vowel(a[i+1][j])==1&&vowel(a[i+1][j+1])==1)
			{
				printf("\n%d - %d",i,j);
				break;
			}
		}
	}return 0;
}
