#include <bits/stdc++.h>
using namespace std;

/**
 * @desc: function that implement Caesar Cipher encoding...
 * @param: string to be encoded and key.
 * @return: encoded string.
 */
string Caesar_Cipher( string str , int key ) {

    string encoded_string = "";

    for( int i = 0 ; i < str.length() ; i++ ) {
        //if the character in the string is in uppercase.
        if( isupper(str[i]) ) {
            encoded_string += ( ( str[i] - 65 + key ) % 26 + 65);   //adding and subtracting the ASCII values is to convert int to char and vice-versa.
        }
        //if the character in the string is in lowercase.
        else if( islower(str[i]) ) {
            encoded_string += ( ( str[i] - 97 + key ) % 26 + 97);
        }
    }

    return encoded_string;
}


int main(void) {

    cout << "Caesar_Cipher( abc , 23 ) = " << Caesar_Cipher("abc" , 23) << endl;

    cout << "Caesar_Cipher( and , 3 ) = " << Caesar_Cipher("and" , 3) << endl;

    cout << "Caesar_Cipher( feel , 4 ) = " << Caesar_Cipher("feel" , 4) << endl;

    return 0;
}


/*
Output:

    Caesar_Cipher( abc , 23 ) = xyz

    Caesar_Cipher( and , 3 ) = dqg

    Caesar_Cipher( feel , 4 ) = jiip

*/
