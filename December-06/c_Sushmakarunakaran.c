#include<stdio.h>
int gcdfinder(int a,int b)
{  int i ,gcd;
    for(i=1; (i <= a) && (i <= b); ++i)
    {
        if(a%i==0 && b%i==0)
            gcd = i;
    }

    return gcd;
}

void main()
{
	int lcm,n1,n2,g;
	printf(" \nenter the numbers to find lcm");
	scanf("%d %d",&n1,&n2);
	g=gcdfinder(n1,n2);
	lcm=(n1*n2)/g;
	printf("\n the LCM is %d",lcm);
}
