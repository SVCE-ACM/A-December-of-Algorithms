# include <stdio.h>
int main(void)
{
  int rowLength, colLength, Steps=99, x, y, m, n;
  printf("\nInput Number Of Rows And Columns : ");
  scanf("%d %d", &rowLength, &colLength);
  int Arr[rowLength][colLength];
  printf("\nInput Matrix:-\n");
   for(int i=0;i<rowLength;i++)
    {
      for(int j=0;j<colLength;j++)
       {
         scanf("%d", &Arr[i][j]);
          if(Arr[i][j]==1)
           {
             x=i;
             y=j;
           }
       }
    }
    for(int i=1, j=1; i<rowLength, j<colLength; i++, j++)
 	   {
 		  m=(x+i)%rowLength;
 		   if(Arr[m][y]==2)
 		    {
 			   if(m>x && Steps>i)
 			    Steps=i;
 			   else if(x>m && Steps>x-m)
 			    Steps=x-m;
 			   else
 			    continue;
 		    }
 		  n=(y+j)%colLength;
 		   if(Arr[x][n]==2)
 	     	{
 		     if(n>y && Steps>i)
 			    Steps=i;
 			   else if(y>n && Steps>y-n)
 			    Steps=y-n;
 			   else
 			    continue;
 	      }
 	   }
 	printf("\nOutput : %d\n", Steps);
 	return 0;
}
