/**
    @Problem:

    You have two triangles ABC and PQR on a plane.
        Your task is to determine whether they are similar.

    In order for two triangles to be similar, any of these three conditions must be true

        1) The sides of triangle ABC are proportional to the sides of PQR. (SSS Rule) AB/PQ = BC/QR = CA/RP

        2) Two sides of the two triangles are proportional and the angle between the sides is the same for both triangles. (SAS Rule) AB/PQ = BC/QR AND angle(ABC) = angle(PQR)

        3) If any two angles of one triangle are equal to any two angles of the other triangle. (AA Rule) angle(ABC) = angle(PQR) AND angle(BCA) = angle(QRP) AND angle(CAB) = angle(RPQ)

     @reference:
            https://www.geeksforgeeks.org/program-to-check-similarity-of-given-two-triangles/

*/

#include <bits/stdc++.h>
using namespace std;

/**
 * @desc: function to check for the condition 1... (side-side-side) (SSS)
 * @param: sides of the two triangles.
 * @return: true if the ratios are equal , false otherwise...
 */
bool check_SSS( int S1[] , int S2[] ) {

    sort( S1 , S1 + 3 );
    sort( S2 , S2 + 3 );

    if( (S1[0] / S2[0] == S1[1] / S2[1]) && (S1[0] / S2[0] == S1[2] / S2[2]) && (S1[1] / S2[1] == S1[2] / S2[2] ) )
        return true;
    return false;

}

/**
 * @desc: function to check for the condition 2... (Side-Angle-Side) (SAS)
 * @param: sides and angles of the two triangles.
 * @return: true if any two sides and it's angle are equal , false otherwise.
 */
bool check_SAS(int S1[] , int S2[] , int A1[] , int A2[]) {

    sort( S1 , S1 + 3 );
    sort( S2 , S2 + 3 );
    sort( A1 , A1 + 3 );
    sort( A2 , A2 + 3 );

    if( ( S1[0] / S2[0] == S1[1] / S2[1] ) && ( A1[2] == A2[2] ) ) {
        return true;
    }

    if( ( S1[1] / S2[1] == S1[2] / S2[2] ) && ( A1[0] == A2[0] ) ) {
        return true;
    }

    if( ( S1[0] / S2[0] == S1[2] / S2[2] ) && ( A1[1] == A2[1] ) ) {
        return true;
    }

    return false;
}

/**
 * @desc: function to check for the condition 3... (Angle-Angle) (AA)
 * @param: angles of two triangles.
 * @return: true if any two angles of the triangles are equal.
 */
bool check_AA(int A1[] , int A2[]) {

    sort( A1 , A1+3 );
    sort( A2 , A2+3 );

    if( (A1[0] == A2[0] && A1[1] == A2[1])
                || (A1[1] == A2[1] && A1[2] == A2[2])
                        || (A1[0] == A2[0] && A1[2] == A2[2])  )
        return true;

    return false;
}

int main(void) {

    int side1[] = { 2 , 3 , 3 };
    int angle1[] = { 80 , 60, 40 };

    int side2[] = { 3 , 6 , 6 };
    int angle2[] = { 40 , 60 , 80 };

    bool sss = check_SSS(side1 , side2);

    bool sas = check_SAS(side1 , side2 , angle1 , angle2);

    bool aa = check_AA(angle1 , angle2);

    if(aa == true ||  sss == true || sas == true)
    {
        cout << "\nTriangles are similar by ";
        if(aa == true) cout << "AA ";
        if(sss == true) cout << "SSS ";
        if(sas == true) cout << "SAS.";
        cout << endl;
    }
    else {
        cout << "\nTriangles are not similar\n";
    }

    return 0;
}


/*
Sample Input/Output:

Input0:
    int side1[] = { 2 , 3 , 3 };
    int angle1[] = { 80 , 60, 40 };

    int side2[] = { 3 , 6 , 6 };
    int angle2[] = { 40 , 60 , 80 };

Output0:

    Triangles are similar by AA SSS SAS.


Input1:
    int side1[] = { 2 , 4 , 4 };
    int angle1[] = { 85 , 45 , 50 };

    int side2[] = { 2 , 5 , 6 };
    int angle2[] = { 40 , 60 , 80 };

Output1:

    Triangles are not similar

*/
