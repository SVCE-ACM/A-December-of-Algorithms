# include <stdio.h>
void main()
{
  int rowLength, colLength, Flag=0;
  printf("\nEnter The Number Of Rows And Columns: ");
  scanf("%d %d", &rowLength, &colLength);
  int Arr[rowLength][colLength];
   for(int i=0;i<rowLength;i++)
    {
      for(int j=0;j<colLength;j++)
       {
         scanf("%d", &Arr[i][j]);
       }
    }
   for(int i=0;i<rowLength-1;i++)
    {
      for(int j=0;j<colLength-1;j++)
       {
         if(Arr[i][j]==Arr[i+1][j+1])
          {
            continue;
          }
         else
          {
            Flag=1;
             break;
          }
       }
    }
   if(Flag==0)
    printf("\nIdentical Diagonals.");
   else
    printf("\nDiagonals are non-identical");
}
