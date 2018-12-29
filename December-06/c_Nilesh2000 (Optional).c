# include <stdio.h>
int calcGCD(int x, int y)
{
  if(y==0)
   return x;
 return calcGCD(y, x%y);
}
long long findLCM(int Array[], int Size)
{
  long long Ans=Array[0];
   for(int i=1;i<Size;i++)
    {
      Ans=(Array[i]*Ans)/calcGCD(Array[i], Ans);
    }
 return Ans;
}
void main()
{
  int n;
  long long Res;
  printf("\nHow Many Integers Do You Want To Input: ");
  scanf("%d", &n);
  int Arr[n];
  printf("\nOptional Input: ");
   for(int i=0;i<n;i++)
    scanf("%d", &Arr[i]);
  Res=findLCM(Arr, n);
  printf("Output: %lli\n", Res);
}
