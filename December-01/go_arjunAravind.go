package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func GetNum () int64 {
	scanner := bufio.NewScanner(os.Stdin) //We first init the 
	_ = scanner.Scan()

	enteredNumber, _ := strconv.ParseInt(scanner.Text(),0,32)
	return enteredNumber
}

func PrintMessage (guess int64, result int8) {
	fmt.Printf("B: I'm guessing it's %v.\n",guess)

	if result == 0 {
		fmt.Printf("A: Nope, sorry, that's less than my number.\n\n")
	} else if result == 1 {
		fmt.Printf("A: No, that's greater than my number.\n\n")
	} else {
		fmt.Printf("A: Wubba Lubba Dub Dub, that's correct!\n\n")
	}
}

func BinarySearch (rangeMin int64, rangeMax int64, firstNumber int64) {

	var middle int64

	for true {

		middle = (rangeMin+rangeMax)/2

		if middle > firstNumber {
			PrintMessage(middle,1)
			rangeMax=middle
		} else if middle < firstNumber {
			PrintMessage(middle,0)
			rangeMin=middle
		} else {
			PrintMessage(middle,2)
			break
		}

	}

}

func main(){

	fmt.Printf("Welcome, players!\n")
	fmt.Printf("Player A, enter your desired number --> ")
	var firstNumber int64 = GetNum()

	fmt.Printf("\nPlayer 2, the system shall now automatically guess for you!\n\n")

	var rangeMax, rangeMin, increment int64
	increment = 1000
	rangeMax = increment
	rangeMin = 0

	for true {

		if rangeMax > firstNumber {
			PrintMessage(rangeMax,1)
			BinarySearch(rangeMin,rangeMax,firstNumber)
			break
		} else if rangeMax < firstNumber {
			PrintMessage(rangeMax,0)
			rangeMin = rangeMax
			rangeMax += increment
		} else {
			PrintMessage(rangeMax,2)
			break
		}

	}
}
