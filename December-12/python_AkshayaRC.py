class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=node(None)

    def append(self,data):
        newnode=node(data)
        curr=self.head
        while not curr.next is None:
            curr=curr.next
        curr.next=newnode

    def print(self):
         curr=self.head
         while not curr is None:
             if curr.data!=None:
                print(curr.data,end=" ")
             curr=curr.next
    def reverse(self):
        prev=None
        curr=self.head
        while not curr is None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev    
lis=linkedlist()
num=int(input("No.of elements"))
print("Enter elements")
for i in range(num):
     lis.append(int(input()))
print("\nGiven linked list")
lis.print()
lis.reverse()
print("\n\nReversed linked list ")
lis.print()        
