#include <iostream>
using namespace std;

/**
  * @desc: function that does binary search algorithm.
  * @param: low, high, number guessed X.
  * @TimeComplexity: O( logN )
  */
void BinarySearch(int low, int high, int X)  {

    while(low <= high) {

        int mid = low + (high - low)/2;   //sometimes (low+high) may get overflow.

        cout << "Guess "<< mid <<" (half of " << low << " to " << high << ") --> ";

        if(mid == X) {
            cout << "Spot on...\n";
            break;
        }
        else if(X < mid) {
            high = mid - 1;
            cout << "you're too high.\n";
        }
        else if(X > mid) {
            low = mid+1;
            cout << "you're too low.\n";
        }

    }

}

int main(void) {

    int X;

    cout << "Player B, please guess the number: ";
    cin >> X;

    cout << "Say my chosen number is " << X << ". What are you going to do? Do a binary search:\n\n";
    BinarySearch( 0, 100, X );  //X considered is in the range, say between 0 and 100.

    return 0;
}

/*
Sample Output:

    Player B, please guess the number: 38
    Say my chosen number is 38. What are you going to do? Do a binary search:

    Guess 50 (half of 0 to 100) --> you're too high.
    Guess 24 (half of 0 to 49) --> you're too low.
    Guess 37 (half of 25 to 49) --> you're too low.
    Guess 43 (half of 38 to 49) --> you're too high.
    Guess 40 (half of 38 to 42) --> you're too high.
    Guess 38 (half of 38 to 39) --> Spot on...

*/
