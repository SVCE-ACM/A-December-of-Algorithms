/*


    The pascal's triangle is given as:

                    1
                1         1
           1        2         1
       1       3         3       1
   1       4        6         4      1


as a 2D matrix:

        i/j |  0   1   2   3   4   5
        -----------------------------
        0   |  1
            |
        1   |  1   1
            |
        2   |  1   2   1
            |
        3   |  1   3   3   1
            |
        4   |  1   4   6   4   1
            |
        5   |  1   5   10  10  5   1


*/


#include <iostream>
using namespace std;

int main(void) {

    int number_of_rows;

    cout << "rows = ";
    cin >> number_of_rows;

    int N = number_of_rows;

    int P[N+1][N+1];

    //calculating pascal triangle 2D Matrix.
    for(int i = 0 ; i <= N ; i++ ) {

        for(int j = 0 ; j <= i ; j++ ) {

            //if it's a first column
            if(j == 0) {
                P[i][j] = 1;
            }
            //if it's a diagonal
            else if( i == j ) {
                P[i][j] = 1;
            }
            //other cells
            else {
                P[i][j] = P[i-1][j-1] + P[i-1][j];
            }

        }
    }

    //printing the pascal's triangle
    cout << endl;

    for(int i = 0 ; i <= N ; i++ ) {
        for(int j = 0 ; j <= i ; j++ ) {
            cout << P[i][j];
        }
        cout << "   --->  row " << i << endl;
    }

    return 0;
}


/*
Sample Input:
    rows = 3

Sample Output:

    1   --->  row 0
    11   --->  row 1
    121   --->  row 2
    1331   --->  row 3

*/


















