#include <stdio.h>
#include<string.h>
#include<ctype.h>
int main()
{
    char p[20];
    int key,i,enc;
    
    printf("Enter Plain text=");
    gets(p);
    printf("\n Enter Key=");
    scanf("%d",&key);
    key=key%26;

    for(i=0;i<strlen(p);i++)
    {
           p[i]=tolower(p[i]);
           enc=((p[i])+key);
           printf("%c",enc);
		   
    }
return 0;    
}

