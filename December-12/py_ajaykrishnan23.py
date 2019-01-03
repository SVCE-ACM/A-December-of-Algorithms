class node:
	def __init__(self,data,nextnode = None):
		self.data = data
		self.next = nextnode
	def setnext(self,nextnode):
		self.next = nextnode
	def getdata(self):
		return self.data
	def setdata(self,val):
		self.data = val
	def getnode(self):
		return self.next

class linkedlist:
	def __init__(self,head = None,nextnode = None):
		self.head = head
		self.next = nextnode
	
	def addnode(self,data):
		newnode = node(data,self.head)
		self.head = newnode
	
	def printnode(self):
		curr = self.head
		while curr.getnode()!=None:
			print(curr.data)
			curr = curr.getnode()
		print(curr.data)
	
	def reverselist(self):
		list1 = []
		curr = self.head
		while curr.getnode()!=None:
			list1.append(curr.getdata())
			curr = curr.getnode()
		list1.append(curr.getdata())
		list1 = list(reversed(list1))
		curr = self.head
		i = 0
		while curr.getnode()!=None:
			curr.setdata(list1[i])
			curr = curr.getnode()
			i+=1
		curr.setdata(list1[i])
			
ll = linkedlist()
n = int(input('Enter number of nodes'))
for i in range(0,n):
	ll.addnode(int(input('Enter data')))
ll.printnode()
ll.reverselist()
print('Reversed list')
ll.printnode()