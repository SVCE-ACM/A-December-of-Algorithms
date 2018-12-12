#include<stdio.h>
#include<stdlib.h>

typedef struct node* Node;
typedef Node loc;
typedef struct table* Table;
struct node {
  int data;
  Node next;
};

struct table {
  int tablesize;
  Node* tble;
};

Node createn(int data) {
  Node newnode=(Node)malloc(sizeof(struct node));
  newnode->data=data;
  newnode->next=NULL;
  return(newnode);
}

int nextprime(int data) {
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
Table inittable(int tsize) {
  Table t=(Table)malloc(sizeof(struct table));
  if(t==NULL) {
    printf("Error\n");
  }
  else {
    t->tablesize=nextprime(tsize);
    t->tble=(Node*)malloc(sizeof(Node)*t->tablesize); //array of pointers
    if(t->tble==NULL) {
      printf("Error\n");
    }
    else {
      for(int i=0;i<t->tablesize;i++) {
        t->tble[i]=createn(i);
        if(t->tble[i]==NULL) {
          printf("Error\n");
        }
      }
    }
  }
  return t;
}

int hashfunc(Table t,int data) {
  int location;
  location=data%t->tablesize;
  return location;
}

void insertdata(Table t, int data) {
  Node location;
  Node newnode=createn(data);
  if(t==NULL) {
    printf("Error\n");
  }
  location=t->tble[hashfunc(t,data)];
  if(location->next==NULL) {
    location->next=newnode;
  }
  else {
    newnode->next=location->next;
    location->next=newnode;
  }
}

void disp(Table t) {
  Node temp;
  for(int i=0;i<t->tablesize;i++) {
    printf("%d\t",i);
    temp=t->tble[i];
    while(temp->next!=NULL) {
      temp=temp->next;
      printf("%d\t",temp->data);
    }
    printf("\n");
  }
}
