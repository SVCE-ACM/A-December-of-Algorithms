#include<stdio.h>
#include<string.h>
int n,k=-1;
char s[10],t[40][10];
void permute(char*,int,int);
void swap(char*,char*);
int main()
{
	int i,f,j;
	char temp[10];
	printf("Enter the string ");
	gets(s);
	n=strlen(s);
	permute(s,0,n);
	for(i=0;i<=k;i++)
	{
		for(j=i+1;j<=k;j++)
		{
			if(strcmp(t[i],t[j])>0)
			{
			    strcpy(temp,t[i]);
			    strcpy(t[i],t[j]);
			    strcpy(t[j],temp);
		    }
		}
	}
	for(i=0;i<=k;i++)
	{
		printf("\n%s",t[i]);
		if(strcmp(t[i],s)==0)
		printf(" --> Match found at position %d",i+1);
    }
	return 0;
}
void permute(char *a,int l,int r)
{
	int i;
	if(l==r)
	{
		strcpy(t[++k],a);
	}    
	else
	{
		for(i=l;i<r;i++)
		{
			swap((a+l),(a+i));
			permute(a,l+1,r);
			swap((a+l),(a+i));
		}
	}
}
void swap(char *x,char*y)
{
	char temp;
	temp=*x;
	*x=*y;
	*y=temp;
}
