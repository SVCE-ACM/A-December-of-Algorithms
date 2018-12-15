#include<stdio.h>    
void towerofhanoi(int n,char a[5],char b[5],char c[5])
{
	if(n==1)
	{
		printf("\n%s to %s",a,c);
		return;
	}	
 towerofhanoi(n-1,a,c,b);
  	printf("\n%s to %s",a,c);
towerofhanoi(n-1,b,a,c); 	
}
void main()
{   int e;
do{
	char l[5]="left", m[5]="mid", r[5]= "right";
	int d;	
	printf("Enter number of discs");
	scanf("%d",&d);
	printf("\n The order of movement of discs:");	
	towerofhanoi(d,l,m,r);
	printf("/n enter 1 to continue and 0 to exit");
	scanf("%d",&e);
}while(e>0);

}

