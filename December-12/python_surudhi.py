def reverseList(list):
       prev = None
       curr = list.head
       nex = curr.getNextNode()
       while curr:
           curr.setNextNode(prev)               
           prev = curr
           curr = nex
           if nex:
               nex = nex.getNextNode()
       list.head = prev
