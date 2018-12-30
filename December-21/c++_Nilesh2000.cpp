# include <iostream>
# include <fstream>
# include <cstdio>
# include <cstdlib>
using namespace std;
int main(void)
{
  ifstream File;
  char fromCountry[100], toCountry[100];
  float Amount;
  cout <<"\nFrom Country: ";
  gets(fromCountry);
  cout <<"Currency I have: ";
  cin >>Amount;
  cout <<"To Country: ";
  getchar();
  gets(toCountry);
  File.open("exchangeRates.csv", ios::in);
   if(!File)
    {
      cout <<"\nError In File Assosciation.";
      getchar();
      exit(0);
    }
  return 0;
}
