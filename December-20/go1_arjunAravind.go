package linkedlist

/**
  * This is a package for linkedlists. It can be used by other classes.
  *
*/

func NewList() List {
	var list List

	list.head = new(node)
	list.head.next = nil

	return list
}

func (list List) Append(value string) {

	if list.Contains(value) {
		return
	}

	temp := new(node)
	temp.next = nil
	temp.value = value

	for pos := list.head; pos != nil; pos = pos.next {
		if pos.next == nil {
			pos.next = temp
			break
		}
	}
}

func (list List) Contains(value string) bool {
	for pos := list.head.next; pos != nil;  pos = pos.next {
		if pos.value == value {
			return true
		}
	}
	return false
}

func (list List) GetIndexOf(value string) int {
	count := 0
	for pos := list.head.next; pos != nil;  pos = pos.next {
		if pos.value == value {
			return count
		}
		count++
	}
	return -1
}

func (list List) GetValueAt(index int) string {
	count := 0

	for pos := list.head.next;  pos != nil; pos = pos.next {
		if count == index {
			return pos.value
		}
		count++
	}

	return "nil"
}
