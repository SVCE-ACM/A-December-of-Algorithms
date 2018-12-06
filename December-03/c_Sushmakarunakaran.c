#include<stdio.h>
void main ()
{ int j; 
 do
{
	long int a;
	int b[10],i=0,count=0,sum1=0,sum2=0;
	  printf(" \n \t \t  enter the ticket number");
	  scanf("%d",&a);
	while(a>0)
	{
		b[i]=a%10;
		i++;
		count++;
		a=a/10;
	}
		if(count%2==0)
		{
			for(i=0;i<(count/2);i++)
				sum1=sum1+b[i];
			for(i=(count/2);i<count;i++)
			    sum2=sum2+b[i];
			if(sum1==sum2)
			    printf("\n \t \t  YEAH!!! you are a LUCKY person");
			else
			    printf("\n \t \t OOPS! try again with another ticket ");	    
		}
		else 
		    printf("\n \t \t enter a valid ticket number");
		printf("\n  enter 1 to check again and 0 to exit ");
		scanf("%d",&j);    
  }while(j==1);
}

