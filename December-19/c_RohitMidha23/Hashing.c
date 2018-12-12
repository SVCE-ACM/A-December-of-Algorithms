#include "SeparateChain.h"
#include "LinearProbing.h"

void main() {
  Table t=NULL;
  LTable lt=NULL;
  int ch=1,op1,op2,op3,tsize,ltsize,data;
  do {
    printf("\n1.Separate Chaining\n2.Linear Probing\n3.Exit ");
    scanf("%d",&op1);
    switch(op1) {
      case 1:
      {
        int ex=1;
        printf("Enter the size of the table ");
        scanf("%d",&tsize);
        t=inittable(tsize);
        printf("Table Created");
        do {
          printf("\n1.Insert\n2.Display\n3.Exit ");
          scanf("%d",&op2);
          switch(op2) {
            case 1:
            {
              printf("Enter the data to be inserted ");
              scanf("%d",&data);
              insertdata(t,data);
              printf("Inserted\n");
              disp(t);
              break;
            }
            case 2:
            {
              disp(t);
              break;
            }
            case 3:
            {
              ex=0;
              break;
            }
          }
        }while(ex==1);
        break;
      }
      case 2:
      {
        int ex2=1;
        printf("Enter the size of the table ");
        scanf("%d",&ltsize);
        lt=initl(ltsize);
        do {
          printf("\n1.Insert\n2.Display\n3.Exit ");
          scanf("%d",&op3);
          switch(op3) {
            case 1:
            {
              printf("Enter the data to insert ");
              scanf("%d",&data);
              insertdatal(lt,data);
              displayl(lt);
              break;
            }
            case 2:
            {
              displayl(lt);
              break;
            }
            case 3:
            {
              ex2=0;
              break;
            }
          }
        }while(ex2==1);
        break;
      }
      case 3:
      {
        ch=0;
        break;
      }
      break;
    }
  }while(ch==1);
}
