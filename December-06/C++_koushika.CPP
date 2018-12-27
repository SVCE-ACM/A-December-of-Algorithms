/*
Author: Koushika Kesavan
Date of Creation: 28 December 2018, Thursday
Title: LCM of 2 numbers
All rights reserved
*/

#include<stdio.h>
#include<conio.h>
#include<iostream.h>
void main()
{
clrscr();
int num1,num2,rem,numerator,denominator,gcd,lcm;
cout<<"\nEnter two numbers:";
cin>>num1>>num2;
if(num1>num2)
{
numerator=num1;
denominator=num2;
}
else if(num2>num1)
{
numerator=num2;
denominator=num1;
}
rem=numerator%denominator;
while(rem!=0)
{
numerator=denominator;
denominator=rem;
rem=numerator%denominator;
}
gcd=denominator;
lcm=(num1*num2)/gcd;
cout<<"\nThe GCD of the 2 numbers are:"<<gcd;
cout<<"\nThe LCM of the 2 numbers are:"<<lcm;
getch();
}
