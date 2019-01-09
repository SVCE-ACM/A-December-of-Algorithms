#include<stdio.h>
#include<stdlib.h>
typedef struct lineartable* LTable;

struct lineartable {
  int ltablesize;
  int* arr;
};

int lnextprime(int data) {
  int flag=0;
    for(int i=data;i<1000;i++) {
      flag=0;
      for(int j=2;j<i/2;j++) {
        if(i%j==0) {
          flag=1;
          break;
        }
      }
      if(flag==0) {
        printf("Size of Table: %d\n",i);
        return i;
      }
    }
}

LTable initl(int tablesize) {
  LTable lt=(LTable)malloc(sizeof(struct lineartable));
  lt->ltablesize=lnextprime(tablesize);
  lt->arr=(int*)malloc(sizeof(int)*lt->ltablesize);
  for(int i=0;i<lt->ltablesize;i++) {
      lt->arr[i]=-1;
  }
  return lt;
}

int hashfuncl(LTable lt,int data) {
  int location;
  location=data%lt->ltablesize;
  return location;
}

void insertdatal(LTable lt,int data) {
  int location,ins=0,temp;
  static int count=0;
  if(count==lt->ltablesize) {
    printf("Full\n");
  }
  else {
    location=hashfuncl(lt,data);
    while(lt->arr[location]!=-1) {
        location=(location+1)%lt->ltablesize;
      }
    lt->arr[location]=data;
    count++;
  }
}

void displayl(LTable lt) {
  for(int i=0;i<lt->ltablesize;i++) {
    printf("%d\t",i);
    if(lt->arr[i]!=-1)
      printf("%d\n",lt->arr[i]);
    else
      printf("\n");
  }
}
