#include <iostream>
using namespace std;

int main()
{
   int num1, num2, i, gcd, lcm;

   cout << "Enter two numbers: " << endl;
   cin >> num1 >> num2;

   //calculation of gcd
   for(i=1; i <= num1 && i <= num2; ++i)
   {
      if(num1 % i == 0 && num2 % i == 0)
      gcd = i;
   }
   //calculation of lcm using gcd
   lcm = (num1 * num2) / gcd;
   cout << "LCM: " << lcm << endl;

   return 0;
}
