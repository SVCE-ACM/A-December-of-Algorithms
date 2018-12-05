package linkedlist

import "fmt"

/**
  * The objective of this program is to first create a linked list and then
  * a function to reverse it. 
*/

type Node struct {
	value string
	next *Node
}

type List struct {
	head *Node
}

/**
  * Creates a List pointer and inits the head pointer
 */
func NewList() *List {
	var list *List
	list = new(List)

	list.head = new(Node)
	list.head.next = nil

	return list
}

/**
  * Adds a node with the given string at the last position
 */
func (list List) Add (value string) {

	var pos *Node
	pos = list.head

	for pos!=nil {
		if pos.next==nil {
			var temp *Node
			temp = new(Node)
			temp.value = value
			temp.next = nil

			pos.next = temp
			break
		}
		pos = pos.next
	}

}

/**
  * Prints the list
 */
func (list List) Print () {

	var pos *Node
	pos = list.head.next

	fmt.Printf("(")

	for pos!=nil {
		fmt.Printf("%v, ", pos.value)
		pos = pos.next
	}

	fmt.Printf("\b\b)\n")

}

/**
  * Prints the length of the list
 */

func (list List) Length () int8 {

	var pos *Node
	pos = list.head.next

	var count int8
	count=0

	for pos != nil {
		count++
		pos = pos.next
	}

	return count
}

/**
  * We store the pointers of the headNode and the firstNode in seperate variables.
  * We then shift every node after the firstNode into the first position. In this way,
  * the list is reversed.
 */
func (list List) Reverse () {

	var firstNode, headNode *Node
	firstNode = list.head.next
	headNode = list.head

	for firstNode.next!=nil {
		var shiftingNode *Node
		shiftingNode = firstNode.next

		firstNode.next = shiftingNode.next //Links end of firstNode to node after shiftingNode
		shiftingNode.next = headNode.next //Links end of shiftingNode to previous first node
		headNode.next = shiftingNode //Links end of headNode to shiftingNode
	}

}

func main() {
	list := NewList()

	list.Add("Arjun")
	list.Add("Aravind")
	list.Add("Divya")
	list.Add("Adnan")
	list.Add("SA")
	list.Add("Aps")

	list.Print()
	list.Reverse()
	list.Print()
}
