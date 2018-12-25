# include <stdio.h>
void main()
{
  int m, n, rowStart=0, colStart=0;
  printf("\nInput Rows And Columns In The Matrix: ");
  scanf("%d %d", &m, &n);
  printf("\nInput Matrix:-\n");
  int i, j;
  int Arr[m][n];
   for(i=0;i<m;i++)
    {
      for(j=0;j<n;j++)
       {
         scanf("%d", &Arr[i][j]);
       }
    }
  int rowLength=m-1;
  int colLength=n-1;
  printf("\nMatrix In Spiral Form:-\n");
    while(rowStart<=rowLength && colStart<=colLength)
     {
       for(i=rowStart;i<=colLength;i++)
        printf("%d --> ", Arr[rowStart][i]);
       for(i=colStart+1;i<=rowLength;i++)
        printf("%d --> ", Arr[i][colLength]);
       for(i=colLength-1;i>=colStart;i--)
        printf("%d --> ", Arr[rowLength][i]);
       for(i=rowLength-1;i>rowStart;i--)
        printf("%d --> ", Arr[i][colStart]);
       rowStart++;
       rowLength--;
       colStart++;
       colLength--;
     }
}
