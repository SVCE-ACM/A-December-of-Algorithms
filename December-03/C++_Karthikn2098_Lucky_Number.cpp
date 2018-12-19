#include <iostream>
#include <stdbool.h>
#include <string>
using namespace std;

/**
  * @desc: function that finds the number is lucky or not.
  * @param: Ticket Number N.
  * @return: true if it is lucky, false otherwise.
  */
bool isLuckyNumber(long long int N) {

    //array that stores the digits of the ticker number.
    int ticket[100];
    int i = 0;

    while(N > 0) {
            ticket[i++] = N % 10;
            N /= 10;
    }

    int length_of_N = i;

    int left_half = 0 , right_half = 0;

    //calculating sum of the right half
    for(int i = 0 ; i < length_of_N/2 ; i++ ) {
        right_half += ticket[i];
    }

    //calculating sum of the left half
    for(int i = length_of_N/2 ; i < length_of_N ; i++ ) {
        left_half += ticket[i];
    }

    if(left_half == right_half)     //if it is lucky number.
        return true;
    return false;
}


int main(void) {

    long long int N;
    string result = "";

    cout << "Enter the Ticket Number: ";
    cin >> N;

    /* A ticket number is considered lucky if the sum of the first half
                        of the digits is equal to the sum of the second half. */
    if( isLuckyNumber(N) )
        result = "true";
    else
        result = "false";

    cout << "isLucky(" << N << ") = " << result;

    return 0;
}

/*
Sample Output:

    Enter the Ticket Number: 1230
    isLucky(1230) = true

    Enter the Ticket Number: 239017
    isLucky(239017) = false

*/
