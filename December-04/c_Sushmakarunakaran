#include<stdio.h>
void main ()
{ int j;
do
{
	int n,num,i,f=0,s=1;
	printf("\n \t \t enter the number of digits to be printed in FIBONACCI series");
	scanf("%d",&num);
	if(num<1)
	 printf("\n \t \t enter a valid number");
	else
	{ 
	   for(i=0;i<num;i++)
	  { 
	   if(i<2)
	    n=i;
	   else
	   {
		n=f+s;
	    f=s;
	    s=n;
           }
	   }   
	    printf("\t %d",n);
      
   }
    printf("\n  enter 1 to print again and 0 to exit");
    scanf("%d",&j);
}while(j==1);
}

