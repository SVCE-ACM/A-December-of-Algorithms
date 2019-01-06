#include <iostream>

using namespace std;

int main()
{
   // 1$ =.72 euro, 1$=0.60gbp, 1$ = 102.15 yen, 1$ = 1.10 CAD
    float AMOUNT;
    cout<<"Enter the amount in Dollar($):- ";
    cin>>AMOUNT;
    int select;
    cout<<" Enter 1 to convert the amount to EURO \n Enter 2 to convert the amount to GBP \n Enter 3 to convert the amount to YEN \n enter 4 to convert the amount to CAD"<<endl;
    cin>>select;
    switch(select)
    {
    case 1:
        cout<<AMOUNT<<" $ = "<<(AMOUNT*0.72)<<" EURO"<<endl;
        break;
    case 2:
        cout<<AMOUNT<<" $ = "<<(AMOUNT*0.60)<<" GBP"<<endl;
        break;
    case 3:
        cout<<AMOUNT<<" $ = "<<(AMOUNT*102.15)<<" YEN"<<endl;
        break;
    case 4:
        cout<<AMOUNT<<" $ = "<<(AMOUNT*1.10)<<" CAD"<<endl;
        break;
    }
return 0;
}
