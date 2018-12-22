/*
    Reversing a given string using recursion.
*/

#include <iostream>
using namespace std;

/**
 * @desc: reverses a string by recursive function.(in-place reversing)
 * @param: string , left most index , right most index.
 */
void reverse_by_recursion( string &str , int left , int right ) {

    if(left > right) {
        return;
    }
    swap(str[left] , str[right]);
    reverse_by_recursion(str , left+1 , right-1);
}

//main function...
int main(void) {

    string str;

    cout << "Enter String: ";
    getline(cin , str);

    reverse_by_recursion(str , 0 , str.length()-1);

    cout << "\nReversed String: " << str;
    return 0;
}

/*

Enter String: string STRING

Reversed String: GNIRTS gnirts

*/


