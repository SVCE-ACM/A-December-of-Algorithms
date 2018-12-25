#include<stdio.h>
void main()
{
	int i,j,n,k;
char s[20];
	printf("Enter the string and the key:");
	scanf("%s%d",s,&k);
	n=strlen(s);
	printf("\n\nEncoded output:");
	for(i=0;i<n;i++)
	{
		k=k%26;
		if(s[i]+k > 122)
		{
			s[i]=s[i]-26;
			printf("%c",s[i]+k);			
		}
		else
		printf("%c",s[i]+k);
	}	
}
