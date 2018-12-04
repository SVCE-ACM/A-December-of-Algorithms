#include<stdio.h>
void main()
{
	long int a;
	int b;    
	do
	{
		int c=0,r,temp,sum1=0,sum2=0,c1;
	printf("Enter your Ticket Number:");
	scanf("%d",&a);
	temp=a;
	while(a>0)
	{		a=a/10;
		c++;	
	}
	if(c%2!=0)
	printf("\nThe ticket number is invalid:");
    c1=c/2;
	while(temp>0)
	{
		r=temp%10;
		if(c<=c1)
		{
		sum1=sum1+r;
		c--;}
		else
{
		sum2=sum2+r;
		c--;}	
		temp=temp/10;	
	}
	if(sum1==sum2)
	{
	printf("--------------------------------------------------------");
	printf("\n\n   wooah you are lucky");
	printf("\n\n----------------------------------------------------");
}
	else
	{
		printf("\n--------------------------------------------------------");
	printf("\n\n better luck next time (^__^)");
		printf("\n\n--------------------------------------------------------");
	}
printf("\n\n\n\t\t\tDo you want to check for another ticket (yes==1) || (no==0) ");
scanf("%d",&b);	
}while(b==1);
}
