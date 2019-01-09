// C++ program to find Deteminant of a matrix 
#include <bits/stdc++.h> 
using namespace std; 
  
// Dimension of input square matrix 
#define N 4 
  
// Function to get cofactor of mat[p][q] in temp[][]. n is current 
// dimension of mat[][] 
void getCofactor(int mat[N][N], int temp[N][N], int p, int q, int n) 
{ 
    int i = 0, j = 0; 
  
    // Looping for each element of the matrix 
    for (int row = 0; row < n; row++) 
    { 
        for (int col = 0; col < n; col++) 
        { 
            //  Copying into temporary matrix only those element 
            //  which are not in given row and column 
            if (row != p && col != q) 
            { 
                temp[i][j++] = mat[row][col]; 
  
                // Row is filled, so increase row index and 
                // reset col index 
                if (j == n - 1) 
                { 
                    j = 0; 
                    i++; 
                } 
            } 
        } 
    } 
} 
  
/* Recursive function for finding determinant of matrix. 
   n is current dimension of mat[][]. */
int determinantOfMatrix(int mat[N][N], int n) 
{ 
    int D = 0; // Initialize result 
  
    //  Base case : if matrix contains single element 
    if (n == 1) 
        return mat[0][0]; 
  
    int temp[N][N]; // To store cofactors 
  
    int sign = 1;  // To store sign multiplier 
  
     // Iterate for each element of first row 
    for (int f = 0; f < n; f++) 
    { 
        // Getting Cofactor of mat[0][f] 
        getCofactor(mat, temp, 0, f, n); 
        D += sign * mat[0][f] * determinantOfMatrix(temp, n - 1); 
  
        // terms are to be added with alternate sign 
        sign = -sign; 
    } 
  
    return D; 
} 
  
/* function for displaying the matrix */
void display(int mat[N][N], int row, int col) 
{ 
    for (int i = 0; i < row; i++) 
    { 
        for (int j = 0; j < col; j++) 
            printf("  %d", mat[i][j]); 
        printf("n"); 
    } 
} 
  
// Driver program to test above functions 
int main() 
{ 
  
    int mat[N][N] = {{4,9,2}, 
                     {3,5,7}, 
                     {8,1,6} 
                    }; 
  
    printf("Determinant of the matrix is : %d", 
            determinantOfMatrix(mat, N)); 
    return 0; 
} 
