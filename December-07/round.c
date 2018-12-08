#include<stdio.h>

round1(float x,float y)
{
	float z;
	z= y-(int )y;	
	if(z>0&& z<=0.5)
	printf("IsApproximatelyEqual(%f, %f) -> true",x,y);
	else if(x==y)
	printf("IsApproximatelyEqual(%f, %f) -> true",x,y);
	else
		printf("IsApproximatelyEqual(%f, %f) -> false",x,y);	
}

roundt(float x,float y)
{
	float t,z;
	printf("\nEnter the tolerance level:");
	scanf("%f",&t);
	z= y-(int )y;
//	printf("\nz=%f",z);
	if(z<=t)
	printf("IsApproximatelyEqual(%f, %f,%f) -> true",x,y,t);
	else
	printf("IsApproximatelyEqual(%f, %f,%f) -> false",x,y,z);
	
	
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
