#include<stdio.h>
int fact(int f)
{

	int fact=1;
	
	while(f>=1)
	{
		fact=fact*f;
		
		f--;
		
	}
	return fact;
}


void print(int n)

{

	int i,j,term;
	int s[30],c=0;
	int b=0,a;
	
	for(i=0;i<n;i++)
	{
		printf("\n");
		printf("row %d ------>",i);
		
		for(j=0;j<=i;j++)
		{
			
		
			term =fact(i)/(fact(j)*fact(i-j));
			
			printf("%d ",term);
			if(n==i+1)
			{
				s[c]=term;
				c++;
				
			}
			
			
		}
	}
	a=i-1;
	printf("\n\n\n");

	for(i=0;i<n;i++)
	{
		printf("%dx^%dy^%d",s[i],a,b);
		if(i!=n-1)
		printf(" + ");
		a--;
		b++;
	}
	


}




void main()
{
	int n;
	
	printf("Enter the number of rows:");
	scanf("%d",&n);
	print(n);

}
