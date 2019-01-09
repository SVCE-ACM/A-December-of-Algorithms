#include <iostream>
using namespace std;

int main()
{
    int n, t1 = -1, t2 = 1, nextTerm = 0;

    cout << "Enter the nth terms: ";
    cin >> n;


    for (int i = 1; i <= n; ++i)
    {
        // Prints the first two terms.

        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }
        cout<<"nth term is :" << nextTerm << " ";
    return 0;
}
