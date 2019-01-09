package main

import "fmt"

type Stack struct {
	arr []int
	top int
	capacity int
}

func NewStack(amt int) Stack {
	stack Stack

	stack.arr = make([]int, amt)
	stack.top = 0
	stack.capacity = amt

	return stack
}

func (stack Stack) Init() {

	for iter := 0; iter < stack.capacity; iter++ {
		stack.arr[iter] = iter+1
	}

}

type solver interface {
    play(int)
}
   
// towers is example of type satisfying solver interface
type towers struct {
    // an empty struct
}
  
// play is sole method required to implement solver type
func (t *towers) play(n int) {    
    t.moveN(n, 1, 2, 3)
}
  
// recursive algorithm
func (t *towers) moveN(n, from, to, via int) {
    if n > 0 {
        t.moveN(n-1, from, via, to)
        t.moveM(from, to)
        t.moveN(n-1, via, to, from)
    }
}
 
func (t *towers) moveM(from, to int) {
    fmt.Println("Move disk from rod", from, "to rod", to)
}
 
func main() {
    var t solver    
    t = new(towers) // type towers must satisfy solver interface
    t.play(4)
}
