# include <iostream>
# include <cstring>
# include <math.h>
using namespace std;
class Permute
{
private:
  char startRange[5];
  char endRange[5];
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
  Permute()
  {
    memcpy(startRange, "Aa0", 3);
    fill(startRange+3, startRange+5, '\0');
    memcpy(endRange, "Zz9", 3);
    fill(endRange+3, endRange+5, '\0');
    Possibilities=calcPossibilityNum(startRange, endRange)+23;
  }
  double getPermutations(string Password)
  {
    double Len = Password.length();
    return pow((double)Possibilities, Len);
  }
  double getSeconds(double Permute, double permutesPerSecond)
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
  cout <<"Maximum time taken to brute-force : " <<Obj.getSeconds(Obj.getPermutations(Password), 500000) <<" seconds\n";
  return 0;
}
