#include<stdio.h>

int main()
{
	
	int a[10][10];
	
	int r,c,i,j,m=0,r1,c1,n=0,p1=0,p2=0,p3=0,p4=0;
	
	int s1=0,s2=0,s3=0,s4=0;
	
	int b1=0,b2=0,b3=0,b4=0;
	
	int d1=0,d2=0,d3=0,d4=0;
	
	int f1,f2;
	
	printf("Enter the no.of rows and columns:");
	scanf("%d%d",&r,&c);
	
	printf("\n \n Enter the elements of the matrix:");
	printf("\n \t");
	
	for(i=0;i<r;i++)
	for(j=0;j<c;j++)
	{
	
	scanf("%d",&a[i][j]);
	if(a[i][j]==1)
	{
	 r1=i;
	 c1=j;
	
	
	m++;}
	if(a[i][j]==2)
	{
		n++;
	}
	
	}
//	 printf("\n r1=%d,c1=%d",r1,c1);    //1 postion
	
//	printf("\n m=%d,n=%d",m,n);          // checking 1 and 2
	
	if(m==1 && n>=1)
	{
		
		
		for(i=c1+1;i<c;i++,p1++)          // left
		{
			//printf("\n a[r1=%d][i=%d]=%d",r1,i,a[r1][i]);
			if(a[r1][i]==2)
			{
				//p1=i-r1;
				p1++;
			
				b1++;
					break;
			}
		
			}
		    	
		if(c1==c-1 )
		{
			
		for(i=0;i<c;i++,p2++)
		{
			if(a[r1][i]==2)
			{
				//p2=i;
				p2++;
				
				b2++;
				break;
			}
			
			
		}
	}
	
	if(b1==0)
	p1=99;
	if(b2==0)
	p2=99;
	
if ( p2>0 && p2>p1 && p2!=99)
{
	p1=p2;
}


	for(i=c1-1;i>=0;i--,p3++)          // right
		{
		
			//printf(" a[r1=%d][i=%d]=%d",r1,i,a[r1][i]);
			if(a[r1][i]==2)
			{
				//p3=c1-i;
				p3++;
			
				b3++;
					break;
			}
		
			
			}
		    	
		if(c1==0 )
		{
			
		for(i=c-1;i>=0;i--,p4++)
		{
			//printf(" a[r1=%d][i=%d]=%d",r1,i,a[r1][i]);
			if(a[r1][i]==2)
			{
				//p4=c-i-1;
				p4++;
			
				b4++;
					break;
			}
		
			
		}
	}
	
	if(b3==0)
	p3=99;
	if(b4==0)
	p4=99;
	
	
	if ( p4>0 && p4<p3 &&p3!=99 )
{
	p3=p4;
}
	
	


//printf("\n p1=%d p2=%d",p1,p2);
//printf("\n p3=%d p4=%d",p3,p4);



for(i=r1+1;i<r;i++,s1++)          // down
		{
			
			//printf("\n a[i=%d][c1=%d]=%d",i,c1,a[i][c1]);
			if(a[i][c1]==2)
			{
				//p1=i-r1;
				s1=s1+1;
				
				d1++;
				//printf("\nd1=%d",d1);
				break;
			}
			
			
			}
		    	
		if(r1==r-1 )
		{
			
		for(i=0;i<r;i++,s2++)
		{
			
			if(a[i][c1]==2)
			{
				//p2=i;
				s2=s2+1;
				
				d2++;
				break;
			}
			
			
		}
	}
//	printf("\n b4 d1=%d",d1);
	if(d1== 0 )
	{
		//printf("\n loop");
			s1=99;
}
	
	if(d2==0)
	s2=99;
	
	//printf("\n s1=%d s2=%d",s1,s2);
	if ( s2>0 && s2>s1 && s2!=99)
{
	s1=s2;
}
	
	
	for(i=r1-1;i>=0;i--,s3++)          // up
		{
			
			//printf("\n a[i=%d][c1=%d]=%d",i,c1,a[i][c1]);
			if(a[i][c1]==2)
			{
				//p1=i-r1;
				s3=s3+1;
			
				d3++;
					break;
			}
		
			}
		    	
		if(r1==0 )
		{
			
		for(i=c-1;i>=0;i--,s4++)
		{
			
			if(a[i][c1]==2)
			{
				//p2=i;
				s4=s4+1;
				
				d4++;
				break;
			}
		
		
		}
	}
	
	if(d3==0)
	s3=99;
	if(d4==0)
	s4=99;
	
	
	if ( s4>0 && s4<s3 && s4!=99)
{
	s3=s4;
}
	//printf("\n s3=%d s4=%d",s3,s4);
	
		f1=(p1<p3)?p1:p3;
	f2=(s1<s3)?s1:s3;
	printf("\n \t OUTPUT: %d",(f1<f2)?f1:f2);
	
	
	
	

}
	else if (m==1 && n ==0)
	printf("\nOUTPUT : 0");
	else
	printf("\n Give proper input:");
	

return 0;	
}
