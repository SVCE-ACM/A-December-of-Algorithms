#include<stdio.h>

round1(float x,float y)
{
	
	float a,b;
	a=x- (int)x;
	//printf("\n a=%f",a);
		b=y- (int)y;
	if(a>0.5)	
	x=(int)x+1;
	else
     x=(int)x;
	if( b>0.5)
	y=(int)y+1;
	else
	y=(int)y;
	
//	printf("\n x=%f",x);
	if( x==y)
	printf("IsApproximatelyEqual(%f, %f) -> true",x,y);
	else
		printf("IsApproximatelyEqual(%f, %f) -> false",x,y);	
}

roundt(float x,float y)
{
	float t,a,b;
	printf("\nEnter the tolerance level:");
	scanf("%f",&t);
		a=x- (int)x;
	printf("\n a=%f",a);
		b=y- (int)y;
	if(a>t)	
	x=(int)x+1;
	else
     x=(int)x;
	if( b>t)
	y=(int)y+1;
	else
	y=(int)y;
		
	if(x==y)
	printf("IsApproximatelyEqual(%f, %f,%f) -> true",x,y,t);
	else
	printf("IsApproximatelyEqual(%f, %f,%f) -> false",x,y,t);
	
	
}



void main()
{
	float a,b;
	int ch;
	do
	{	
	printf("\n\n\n1.withot Tolerence level\n2.with Tolernce level\n3.exit\n\n\t\t\tEnter your choice:");
	scanf("%d",&ch);	
	printf("Enter the 1st number:");
	scanf("%f",&a);
	printf("\nEnter the 2nd number to check with first:");
	scanf("%f",&b);	
	switch(ch)
	{
		case 1:
			{
			
			round1(a,b);
			break;}
			
		case 2:			
				{			
		    roundt(a,b);
		    break;
		}
		
			
	printf("\nch=%d",ch);
	
}
}while(ch<=2);
}
