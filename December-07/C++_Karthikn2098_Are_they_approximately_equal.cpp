#include <iostream>
#include <string>
#include <stdbool.h>
using namespace std;

/**
  * @desc: function that round-off the given floating point number.
  * @param: floating number N.
  * @return: rounded integer.
  */
int round_off(double N) {

    //if the N is negative
    if(N < 0)
        return N - 0.5;

    //if the N is positive.
    if(N > 0)
        return N + 0.5;
}

/**
  * @desc: function to check the two numbers are approximately equal without the Tolerance Level.
  * @param: two numbers, say N1 & N2
  * @return: true if they are approximately equal, false otherwise.
  */
bool IsApproximatelyEqual(float N1, float N2)  {

    if(round_off(N1) == round_off(N2))
        return true;
    return false;

}


/**
  * @desc: function to check the two numbers are approximately equal with the Tolerance Level.
  * @param: two numbers, say N1 & N2, Tolerance level.
  * @return: true if they are approximately equal with the given threshold level, false otherwise.
  */
bool IsApproximatelyEqual(float N1, float N2, float TL)  {

    float differnce = N1 > N2 ? N1 - N2 : N2 - N1;

    if(differnce > TL)
        return false;
    return true;
}



int main(void) {

    float num1, num2, tl;
    string result_1 = "", result_2 = "";

    cout << "Enter number1 & number2 & Tolerance Level: ";
    cin >> num1 >> num2 >> tl;

    result_1 = IsApproximatelyEqual(num1, num2) ? "true" : "false";
    result_2 = IsApproximatelyEqual(num1, num2, tl) ? "true" : "false";

    cout << "\nWithout Tolerance Level: \nIsApproximatelyEqual( " << num1 << " , " << num2 << " )" << " --> " << result_1 << endl;

    cout << "\nWith Tolerance Level: \nIsApproximatelyEqual( " << num1 << " , " << num2 << " , " << tl << " )" << " --> " << result_2 << endl;
    return 0;
}


/*
SampleOutput:

    Enter number1 & number2 & Tolerance Level: 3.0 2.5706 0.01

    Without Tolerance Level:
    IsApproximatelyEqual( 3 , 2.5706 ) --> true

    With Tolerance Level:
    IsApproximatelyEqual( 3 , 2.5706 , 0.01 ) --> false

*/
