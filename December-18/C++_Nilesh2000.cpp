# include <iostream>
# include <string.h>
# include <math.h>
using namespace std;
class Permute
{
private:
  char startRange[3];
  char endRange[3];
  int Possibilities;
  int calcPossibilityNum(char startRange[], char endRange[])
  {
		int Len=strlen(startRange);
		int Sum=0;
		 for(int i=0;i<Len;i++)
      {
			  int Range=endRange[i]-startRange[i];
			  Sum+=Range;
		  }
		return Sum;
	}
public:
  void initVars()
  {
    startRange[3]="Aa0";
    endRange[3]="Zz9";
    Possibilities=calcPossibilityNum(startRange, endRange)+23;
  }
 double getPermutations(string Password)
 {
   double Len = Password.length();
   return pow((double)Possibilities, Len);
 }
 double GetSeconds(double Permute, double permutesPerSecond)
 {
   return (Permute/permutesPerSecond);
 }
};
int main(void)
{
  string Password;
  cout <<"\nEnter Password : ";
  cin >>Password;
  Permute Obj;
  cout <<"Maximum time taken to brute-force : " <<Obj.getPermutations(Password);
  return 0;
}
