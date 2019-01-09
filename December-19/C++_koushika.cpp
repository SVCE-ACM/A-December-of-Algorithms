#include <iostream>
#include <string.h>
#include<stdio.h>

using namespace std;

int main()
{
    int hash = 7,i;
    char str[50];
    gets(str);
    for (i = 0;i<strlen(str);i++)
    {
    hash = hash + str[i];
    }
    puts(str);
    cout<<"Hash code of the string:"<<hash;
    return 0;
}
