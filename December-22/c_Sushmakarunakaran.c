#include<stdio.h>
#include<string.h>
int main()
{
	int i,j,k,n,w[25];
	char a[100],b[25][25],temp[25];
	printf("Enter a sentence: ");
	gets(a);
	puts(a);
	for(k=0,i=0;a[k]!='\0';i++)
	{
		j=0;
		while(a[k]!=' '&&a[k]!='\0')
		{
			b[i][j]=a[k];
			if(b[i][j]>=65&&b[i][j]<=90)
			b[i][j]+=32;
			j++;
			k++;
		}
		b[i][j]='\0';
		k++;
	}
	n=i;
	k=0;
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++)
		{
			if(strcmp(b[i],b[j])>0)
			{
			    strcpy(temp,b[i]);
			    strcpy(b[i],b[j]);
			    strcpy(b[j],temp);
		    }
		}
	}
	i=0;
    while(i<n-1)
    {
	    w[k]=1;
      	for(j=i+1;j<n;j++)
       	{
         	if(strcmp(b[i],b[j])==0)
    	        w[k]++;	
			else 
			break;	
	    }
	    printf("\n%d\t%s",w[k],b[i]);
	    k++;
		i=j;
    }	
	return 0;
}

