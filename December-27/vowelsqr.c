#include<stdio.h>
#include<string.h>

void main()
{
	char a[20][20];
	
	int n,i,l,j,c=0,o=0;
	
	
	
	printf("Enter the no.of Strings and size:");
	scanf("%d %d",&n,&l);
	printf("\nEnter the strings:");
	for(i=0;i<n;i++)
	{
		 scanf(" %[^\n]",a[i]);
		 
		
	}

	
	for(i=0;i<n;i++)
	for(j=0;j<l;j++)
	{


		if(a[i][j]=='a'|| a[i][j]=='e'|| a[i][j]=='i'|| a[i][j]=='o' || a[i][j]=='u')
		{
			if(a[i+1][j]=='a'|| a[i+1][j]=='e'|| a[i+1][j]=='i'|| a[i+1][j]=='o' || a[i+1][j]=='u' || i+1>n)
			{
	
			c++;}
			if(a[i-1][j]=='a'|| a[i-1][j]=='e'|| a[i-1][j]=='i'|| a[i-1][j]=='o' || a[i-1][j]=='u' || i-1<0 ) 
			{
	
			c++;}
		
			if(a[i][j+1]=='a'|| a[i][j+1]=='e'|| a[i][j+1]=='i'|| a[i][j+1]=='o' || a[i][j+1]=='u' ||  j+1>n){
		
			c++;}
			if(a[i][j-1]=='a'|| a[i][j-1]=='e'|| a[i][j-1]=='i'|| a[i][j-1]=='o' || a[i][j-1]=='u'||  j-1<0){
			
	
			c++;}
			if(a[i+1][j+1]=='a'|| a[i+1][j+1]=='e'|| a[i+1][j+1]=='i'|| a[i+1][j+1]=='o' || a[i+1][j+1]=='u' || i+1>n ||  j+1>n){
			
		
			c++;}
		
			if(c==5)
			{
			
			printf("\n%d-%d",i,j);
			break;
			o++;
			
	
}
else
c=0;
		
			
			 
		}
	}
	
if(o!=0)
printf("\n unavailable");



}
	

