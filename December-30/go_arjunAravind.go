package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func GetValue() int {

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	enteredNumber, _ := strconv.Atoi(scanner.Text())
	return enteredNumber

}

func main() {

	fmt.Printf("Enter the number of sides --> ")
	sides := GetValue()

	diagonals := (sides * (sides-3)) / 2 //Figured out this formula myself
	fmt.Printf("The number of diagonals is %v.\n", diagonals)

}
