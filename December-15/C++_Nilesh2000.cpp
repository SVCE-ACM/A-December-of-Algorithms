# include <iostream>
using namespace std;
void printPascal(int r)
{
  int Arr[r][r];
  cout <<"\n";
   for(int Line=0;Line<r;Line++)
    {
      for(int i=0;i<=Line;i++)
       {
         if(i==Line || i==0)
            Arr[Line][i]=1;
         else
            Arr[Line][i]=Arr[Line-1][i-1]+Arr[Line-1][i];
         cout <<Arr[Line][i] <<" ";
       }
       for(int j=Line;j<=r;j++)
        cout <<" ";
      cout <<"\t--> Row " <<Line;
      cout <<"\n";
    }
  cout <<"\nPolynomial : ";
  cout <<"\n";
}
int main(void)
{
  int Rows;
  cout <<"\nInput Number Of Rows : ";
  cin >>Rows;
  printPascal(Rows+1);
}
