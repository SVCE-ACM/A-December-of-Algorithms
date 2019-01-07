#include <stdio.h>
#include <math.h>
void roundoff(float x, float y)
{
	int a,b;
	a = round (x);
	b= round(y) ;
	if (a==b)
	   printf(" \n \t \t the two numbers are approximately equal");
	else
	   printf(" \n \t \t the numbers are not approximately equal");
}
void manualroundoff (float x , float y , float z)
{
	float a , b ;
	int c ,d ;
	c=x;
	d=y;
	a= x-c;
	b= y-d;
	if((a>0.5)&&(a<=z)) 
	{ 
	  c=c+1;
	}
	
	if((b>0.5)&&(b<=z))
	{
		d=d+1;
	}
	
	if(c==d)
	   printf(" \n \t \t the two numbers are approximately equal");
	else
	   printf(" \n \t \t the numbers are not approximately equal");
}
void manualroundofft (float x , float y , float z)
{
	float a ,  b ;
	int c ,d ;
	c=x;
	d=y;
	a= x-c;
	b= y-d;
	if((a>z)&&(a<=0.999)) 
	{ 
	  c=c+1;
	  
	}
	
	if((b>z)&&(b<=0.999))
	{
		d=d+1;
		
	}
	
	if(c==d)
	   printf(" \n \t \t the two numbers are approximately equal");
	else
	   printf(" \n \t \t the numbers are not approximately equal");
}

void main ()
{ int g;
do
{
    float e,f,t;
	int s;
	printf(" \n \t \t enter the two numbers");
	scanf("%f %f",&e,&f);
	printf("\n enter \t\t 1 for built in function \n \t\t 2 for manual roundoff checking \n \t\t 3 for checking with tolerance level");
	scanf("%d",&s);
	switch (s)
	{
		case 1 :
			   {
			   	roundoff(e,f);
			   	break ;
			   }
		case 2:
		       {
		       	manualroundoff(e,f,0.99999);
		       	break ;
			   }
		case 3 :
		       {
		       	printf("\n \t \t enter the tolrance level");
		       	scanf("%f",&t);
		       	manualroundofft(e,f,t);
		       	break ;
		       }	   	   
	}
	printf("\n \t \t enter 5 to exit and 4 to continue");
	scanf("%d",&g);
}while(g<5);
}
