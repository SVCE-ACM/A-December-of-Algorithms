#include<stdio.h>
#include<string.h>



void encryptanddecrypt(char s[],int n)
{
	//printf("%s",s);
	char a[26],c;
	int i =0,j=0;
	for(c='a';c<='z';c++)
	{
		a[i]=c;
	//	printf("\na[%d]= %c",i,a[i]);
		i++;
	}
	for(c='a';c<='z'&& j<=n ;c++)
	{
		if(c==s[j])
		{
			
			s[j]=c+n;
			//printf("s %d =%c",j,s[j]);
			c = 'a';
			j++;
			
			
			
		}
	}
	
	
printf("\nEncoded output=%s",s);	
	
}



int main()
{
	int i,j,n,k;

char s[20];
	printf("Enter the string and the key:");
	scanf("%s%d",s,&k);
	n=strlen(s);
    	//printf("%s %d",s,k);
    encryptanddecrypt(s,n);	
    	
return 0;	
}
