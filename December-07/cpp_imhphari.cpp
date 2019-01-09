#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

bool approx_equal(double x, double y)
{
   const double e=1E-1;
   if (x == 0) return fabs(y)<=e;
   if (y == 0) return fabs(x)<=e;
   return fabs(x - y)/max(fabs(x),fabs(y))<=e;
}

int main()
{
   double x;
   cout << "Enter first number: ";
   cin >> x;

   double y;
   cout << "Enter second number: ";
   cin >> y;

   double th;
   cout<<"Enter tolerance level: ";
   cin>>th;


   if(approx_equal(x,y)){
        if((fabs(x)-fabs(y))<th){
            cout << "Less than tolerance level....The numbers are approximately equal.\n";
            }

        else
            cout << "Greater than tolerance level.... The numbers are different.\n";}

   return 0;
}

