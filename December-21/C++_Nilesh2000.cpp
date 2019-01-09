# include <fstream>
# include <iostream>
# include <cstdlib>
# include <cstring>
using namespace std;
const int numOfCountries=55;
struct Exchange
{
  char Country[100];
  float rateOfExchange;
};
int main()
{
  ifstream File;
  char Str[100], fromCountry[100], toCountry[100];
  float Amount, convertAmount;
  Exchange Obj[numOfCountries];
  int i=0, Flag=0;
  cout <<"\nFrom Country : ";
  gets(fromCountry);
  cout <<"Currency I Have : ";
  cin >>Amount;
  cout <<"To Country : ";
  getchar();
  gets(toCountry);
  File.open("exchangeRates.csv", ios::in);
   if(!File)
    {
      cout <<"\nError In File Assosciation.";
      getchar();
      exit(0);
    }
  File.getline(Str, 100);
   while(File.eof()==0)
    {
      File.getline(Str, 100, ',');
      strcpy(Obj[i].Country, Str);
      File.getline(Str, 100);
      Obj[i].rateOfExchange=atof(Str);
      i++;
       if(File.eof()==true)
        break;
    }
   for(i=0;i<numOfCountries;i++)
    {
      if(strcmp(fromCountry, Obj[i].Country)==0)
       {
         for(int j=0;j<numOfCountries;j++)
          {
            if(strcmp(toCountry, Obj[j].Country)==0)
             {
               convertAmount=(Amount/Obj[i].rateOfExchange)*Obj[j].rateOfExchange;
               Flag=1;
               break;
             }
          }
         if(Flag==1)
          break;
       }
    }
  cout  <<'\n' <<Amount <<" (" <<fromCountry <<") = " <<convertAmount <<" (" <<toCountry <<")" <<'\n';
  File.close();
  return 0;
}
