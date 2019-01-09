#include<stdio.h>
int main()
{
	int c,i,j;
	float a,b,t;
	printf("Approximately equal");
	printf("\n1. With threshold level\n2. Manual rounding\n");	
	scanf("%d",&c);
	printf("Enter two numbers ");
	scanf("%f%f",&a,&b);
	if(c==1)
	{
		printf("Tolerance level ");
	    scanf("%f",&t);
	    if((a-b)<t&&(a>b)||(b-a)<t&&(b>a))
	    printf("They are approximately equal");
	    else
	    printf("False as the difference is more than tolerance level");
	}
	else if(c==2)
	{
		i=a;j=b;
	    if(a-i>0.5)
	    i++;
	    if(b-j>0.5)
	    j++;
	    if(i==j)
	    printf("They are approximately equal");
	    else
	    printf("They are not approximately equal");
	}
	else
	printf("Invalid choice");
	return 0;
}

