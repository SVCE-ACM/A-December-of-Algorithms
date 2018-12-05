#include<stdio.h>    
void tower(int n,char source[],char inter[],char dest[])
{
	if(n==1)
	{
		printf("\n%s->%s",source,dest);
		return;
	}	
 tower(n-1,source,dest,inter);
  	printf("\n%s->%s",source,dest);
tower(n-1,inter,source,dest); 	
}
void main()
{
	char l[10]="left";
	char m[10]="middle";
	char r[10]="right";
	int d;	
	printf("Enter the no. of disc:");
	scanf("%d",&d);
	printf("\n\n\n The order in which the disc in source reach to destination is:");	
	tower(d,l,m,r);	
}
