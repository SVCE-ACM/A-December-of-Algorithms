//matrix diagonal elements sum c++

#include<iostream.h>
#include<conio.h>
void main()
{
          int a[10][10],*p[10];
          int m,n,i,j,s1=0,s2=0,t;
          cout<<"Enter the order of matrics: ";
          cin>>m>>n;
          cout<<"Enter the elements\n\n";
          for(i=0;i<m;i++)
          {
                   p[i]=&a[i][0];
                   for(j=0;j<n;j++)
                   {
                             cin>>a[i][j];
                   }
          }
          cout<<"\n\nFirst diagonal elements are\n\n";
          for(i=0;i<n;i++)
          {
                   cout<<*(p[i]+i)<<"\t";
                   s1=s1+*(p[i]+i);
          }
          cout<<"\n\nSecond diagonal elements are\n\n";
          t=n;
          for(i=0;i<n;i++)
          {
                   cout<<*(p[t-1]+i)<<"\t";
                   s2=s2+*(p[t-1]+i);
                   t--;
          }
          cout<<"\n\nSum of first diagonal elements is: ";
          cout<<s1;
          cout<<"\n\nSum of second diagonal elements is: ";
          cout<<s2;
          if(sum1==sum2)
          {
          cout<<"\nThe diagonals are identical";
          }
          else
          {
          cout<<"\nThey are not";
          }
          getch();

}
