/*

Problem:-

    Return the least common multiple of two or more numbers.

    Use the greatest common divisor (GCD) formula ,

        lcm(x,y) = x * y / gcd(x,y).

*/

#include <bits/stdc++.h>
using namespace std;

/**
 * @desc: function to find of the GCD of two numbers by euclidean algorithm.
 * @param: two numbers say N1 , N2.
 * @return: GCD of N1 , N2.
 */
int two_numbers_gcd(int N1 ,int N2) {


    int dividend = N1;
    int divisor = N2;
/*
    while( divisor != 0 ) {
        int remainder = dividend % divisor;
        dividend = divisor;
        divisor = remainder;
    }

    return dividend;
*/

    //the above commented lines of code using recursion...
    return N2 == 0 ? N1 : two_numbers_gcd( N2 , N1%N2 );
}

/**
 * @desc: function to find of the LCM of two numbers by using GCD.
 * @param: two numbers say N1 , N2.
 * @return: LCM of N1 , N2.
 */
int two_numbers_lcm(int N1 , int N2) {
    return (N1 * N2) / two_numbers_gcd(N1 , N2);
}


//main function...
int main() {
    int num1 , num2;

    cout << "Enter two numbers to compute LCM: ";
    cin >> num1 >> num2;

    cout << "LCM is... " << two_numbers_lcm(num1 , num2);
}
