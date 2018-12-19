/*
    fibonacci numbers... 0 1 1 2 3 5 8 13 21 34 55
*/

#include <iostream>
using namespace std;

/**
 * @desc: function to generate N FIBONACCI NUMBERs.
 * @param: N
 * @return: Nth fibonacci number.
 */
int FIBONACCI(int N) {
    //array that stores the fibonacci numbers.
    int fib[N+1];

    fib[0] = 0;
    fib[1] = 1;

    for(int i = 2 ; i <= N ; i++ ) {
        fib[i] = fib[i-1] + fib[i-2];   //by definition of fibonacci no.
    }
    return fib[N];
}


int main(void) {

    int N;

    cout << "Enter N to get Nth fibonacci number: ";
    cin >> N;

    cout << "The " << N << "th fibonacci number is " << FIBONACCI(N) << '.';
    return 0;
}


/*
Sample Output:

    Enter N to get Nth fibonacci number: 10
    The 10th fibonacci number is 55.

*/
