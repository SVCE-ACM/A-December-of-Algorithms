#include<stdio.h>
void main ()
{
	int a[5][5],i,j,r,c,m,n,x,y,s=99,t=99,u=99,v=99,z,e;
	printf("\n enter the number of rows and columns");
	scanf("%d %d",&r,&c);
	printf("\n Enter the elements only 0s 1 and 2");
	printf("\n RULE : enter 1 only once");
	for(i=0;i<r;i++)
	 {
	 	for(j=0;j<c;j++)
	 	{
		   scanf("%d",&a[i][j]);
		    if(a[i][j]==1)
	 	   {
	 	  	m=i;
	 	  	n=j;
	 	   }
	    } 
    }
    x=m;
    y=n;
for(i=1;i<r;i++)
{   
	if((x+i)<r)
	{ m=x+i;
	if(a[m][n]==2)
	  s=i;
	  break;
    }
}
 for(j=1;j<r;j++)   
    {
    	m=x-j;
    if(a[m][n]==2)
	  t=j;
	  break;
	}
for(i=1;i<c;i++)
{   
	if((y+i)<c)
	{ n=y+i;
	if(a[x][n]==2)
	  u=i;
	  break;
    }
}
 for(j=1;j<c;j++)   
    {
    	n=y-j;
    if(a[x][n]==2)
	  v=j;
	  break;
	}
	z=(s<t)?s:t;
	e=(u<v)?u:v;
	printf("\n \t \t %d",(z<e)?z:e);
	
}

		
 

    

