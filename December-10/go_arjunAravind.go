package main

import (
	"fmt"
	"os"
	"bufio"
	"strconv"
)

func GetNum() int {
	fmt.Printf("Enter a number --> ")

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	enteredText := scanner.Text()
	enteredNumber, err := strconv.Atoi(enteredText)

	if err != nil {
		fmt.Printf("Oops! You seem to have entered a wrong value! Try again!\n\n")
		return GetNum()
	}

	return enteredNumber
}

func main() {

	a := GetNum()
	b := GetNum()
	c := GetNum()
	d := GetNum()

	fmt.Printf("The determinant is --> %v\n", (a*d)-(b*c))

}
