/*

    Given a Matrix of size M * N, output its elements in spiral form.

            01     02     03
            04     05     06
            07     08     09

    The Spiral form of a matrix is as below.

    01 --> 02 --> 03 --> 06 --> 09 --> 08 --> 07 --> 04 --> 05

    Move Right, Move Down, Move Left, Move Up till you cover all elements of matrix.

*/

#include <bits/stdc++.h>
using namespace std;

/**
 * @desc: algorithm to print the matrix in a spiral form.(using four direction indices)
 * @param: 2D-array , no of rows , no of columns.
 * @return: spiral form of the given 2D array as 1D array.
 */


//main function
int main(void) {

    int rows , columns;

    //getting rows.
    cout << "Enter the no of rows: ";
    cin >> rows;

    cout << endl;

    //getting columns.
    cout << "Enter the no of columns: ";
    cin >> columns;

    //declaring 2D array
    int arr[rows][columns];


    //getting matrix elements...

    cout << "\nEnter the Matrix: \n";

    for( int i = 0 ;  i < rows ; i++ ) {
        for( int j = 0 ; j < columns ; j++ ) {
            cin >> arr[i][j];
        }
    }


    //calculating the spiral matrix and storing it in 1D array...
    int *result = (int*) malloc(sizeof(int) * (rows * columns));

    int TOP = 0 , BOTTOM = rows - 1 , LEFT = 0 , RIGHT = columns - 1;

    int direction = 0;  //initial direction

    int index = 0;

    while( TOP <= BOTTOM && LEFT <= RIGHT ) {

        //traversing from left to right...
        if( direction == 0 ) {
                for( int i = LEFT ; i <= RIGHT ; i++ ) {
                    result[index++] = *( *(arr + TOP) + i );
                }
                TOP++;
        }
        //traversing from top to bottom...
        else if( direction == 1 ) {
                for( int i = TOP ; i <= BOTTOM ; i++ ) {
                    result[index++] = *( *(arr + i) + RIGHT );
                }
                RIGHT--;
        }
        //traversing from right to left...
        else if( direction == 2 ) {
                for( int i = RIGHT ; i >= LEFT ; i-- ) {
                    result[index++] = *( *(arr + BOTTOM) + i );
                }
                BOTTOM--;
        }
        //traversing from bottom to top...
        else if( direction == 3 ) {
                for( int i = BOTTOM ; i >= TOP ; i-- ) {
                    result[index++] = *( *(arr + i) + LEFT );
                }
                LEFT++;
        }

        //circulating the direction
        direction = (direction + 1)%4;

    }


    cout << "\nThe Spiral form of a matrix is... \n\n";

    for(int i = 0 ; i < rows * columns ; i++ ) {
        cout << result[i] << ' ';
    }

    return 0;
}


/*
Sample Input/Output:

    Enter the no of rows: 3

    Enter the no of columns: 3

    Enter the Matrix:
    1 2 3
    4 5 6
    7 8 9

    The Spiral form of a matrix is...

    1 2 3 6 9 8 7 4 5

*/





















