#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
class Node:


    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev



    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node



    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,"-->",end=" ")
            temp = temp.next


def main():
  llist = LinkedList()
  num=int(input("ENTER NUMBER OF NODES:"))
  for i in range(0,num):
      node=int(input("ENTER NODE:"))
      llist.push(node)


  print("Given Linked List")
  llist.printList()
  llist.reverse()
  print("\nReversed Linked List")
  llist.printList()

if __name__ == '__main__':
    main()
