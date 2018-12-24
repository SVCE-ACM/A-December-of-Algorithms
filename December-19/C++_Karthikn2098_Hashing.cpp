/*

    Implement a hash function that takes a string of variable length and
                        returns an integer with a fixed maximum number of digits.

    The simplest method would be to just use a 3-digit length of the string.
                        001, 042, 340 for 1, 42 and 340 characters respectively.

*/


#include <bits/stdc++.h>
using namespace std;

/**
 * @desc: function that converts the given string to integer.
 * @param: number as a String.
 * @return: the converted integer.
 */
long long int string_to_int_hash(string str) {

    long long int sum = 0;

    for(int i = 0 ; i < str.length() ; i++ ) {
        sum = sum * 10 + (str[i] - '0');
    }

    return sum;
}


int main(void) {

    long long int N1 = string_to_int_hash("001");
    long long int N2 = string_to_int_hash("042");
    long long int N3 = string_to_int_hash("340");
    long long int N4 = string_to_int_hash("2521");
    long long int N5 = string_to_int_hash("10000");

    cout <<"N1 = " << N1 << "\nN2 = " << N2 << "\nN3 = " << N3  << "\nN4 = "<< N4 << "\nN5 = "<< N5;

    return 0;
}

/*
Output:

    N1 = 1
    N2 = 42
    N3 = 340
    N4 = 2521
    N5 = 10000

*/














