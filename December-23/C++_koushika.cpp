#include <iostream>
#include <string.h>
#include<stdio.h>
#include<math.h>

using namespace std;

struct departments
{
char code[3];
int ds;
int num=1;
};

struct seating
{
char code[3];
int num;
};

int main()
{
    int nc,cc,i,nd,j,index,count=1,k,l;
    departments s[10];
    cout<<"\nEnter number of classrooms:";
    cin>>nc;
    cout<<"\nEnter capacity of classrooms:";
    cin>>cc;
    index=sqrt(cc);
    seating mat[index][index];
    cout<<"\nEnter no. of departments:";
    cin>>nd;
    for(i=0;i<nd;i++)
    {
        cout<<"\nEnter department code and strength:";
        cin>>s[i].code>>s[i].ds;
    }
    for(i=0;i<nc;i++)
     {
         for(j=0;j<index;j++)
          {
              for(l=0;l<index;l++)
              {
                k=0;
                while(k<nd)
                {
                    if((strcmp(s[k].code,mat[j-1][l].code)!=0) && (strcmp(s[k].code,mat[j][l-1].code)!=0) && (strcmp(s[k].code,mat[j+1][l].code)!=0) && (strcmp(s[k].code,mat[j][l+1].code)!=0))
                    {
                        strcpy(mat[j][l].code,s[k].code);
                        mat[j][l].num=s[k].num;
                        s[k].num++;
                        break;
                    }
                    k++;
                }
              }
          }
          cout<<"\nRoom "<<i+1; 
         for(j=0;j<index;j++)
          {
              cout<<"\n";
              for(l=0;l<index;l++)
              {
                  cout<<j<<l<<mat[j][l].code<<mat[j][l].num<<" ";
                  strcpy(mat[j][l].code,"a");
                  mat[j][l].num=0;
              }
          }
     }
return 0;
}
