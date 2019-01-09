package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func GetValue () int {

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	enteredNumber, _ := strconv.Atoi(scanner.Text())
	return enteredNumber

}

func Fact(num int) int64 {
	var number, fact, iter int64

	number = int64(num)
	fact = 1

	for iter = number; iter > 0; iter-- {
		fact *= iter
	}

	return fact
}

func main() {

	var cups int

	fmt.Printf("Enter the number of cups --> ")
	cups = GetValue()

	strings := Fact(cups) / ( 2 * Fact(cups-2) )

	fmt.Printf("The number of strings is %v.\n", strings)
}
