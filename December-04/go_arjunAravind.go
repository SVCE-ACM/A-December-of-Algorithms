package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

/**
  * The objective of this program is to make sure that we can find the
  * nth number in the fibonacci series.
*/

func GetNum() int64 {

	fmt.Printf("Enter a number --> ")

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()
	var enteredText string = scanner.Text()

	var enteredNum int64
	enteredNum, err := strconv.ParseInt(enteredText,0,64)

	if err != nil {
		fmt.Printf("The number seems to be invalid. Try again!\n\n")
		return GetNum()
	} else if enteredNum <= 0 {
		fmt.Printf("The number can't be < or = to 0. Try again!\n\n")
		return GetNum()
	}

	return enteredNum

}

func GetFibonacci (number int64) int64 {

	var firstNum, secondNum, thirdNum, iter int64

	firstNum = -1
	secondNum = 1

	for iter=0; iter<number; iter++ {
		thirdNum = firstNum + secondNum
		firstNum = secondNum
		secondNum = thirdNum
	}

	return thirdNum

}

func main() {

	var n int64
	n = GetNum()

	fmt.Printf("Element %v of the Fibonacci series is %v.\n",n,GetFibonacci(n));

}
