package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

/**
  * The objective of this program is to find if a given number is a
  * lucky number or not. This can be found out by checking if the first
  * half of the digits of the number is equal to the second half.
*/

func GetNum() string {
	fmt.Printf("Enter a number --> ")

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	var enteredText string = scanner.Text()
	var length int = len(enteredText)

	_, err := strconv.ParseInt(enteredText,0,64)

	if length%2!=0 {
		fmt.Printf("Your number should have an even number of digits. Try again!\n\n")
		return GetNum()
	} else if err!=nil {
		fmt.Printf("You seem to have entered an invalid value. Try again!\n\n")
		return GetNum()
	}

	return enteredText
}

func FirstHalfSum (number string) int64 {

	var stringRange int
	stringRange = len(number)/2

	var sum int64
	sum = 0

	for iter:=0; iter<stringRange; iter++ {
		digit, _ := strconv.ParseInt(string(number[iter]),0,64)
		sum += digit
	}

	return sum

}

func SecondHalfSum (number string) int64 {

	var stringStart, length int
	length = len(number)
        stringStart = length/2

        var sum int64
	sum = 0

        for iter:=stringStart; iter<length; iter++ {
                digit, _ := strconv.ParseInt(string(number[iter]),0,64)
                sum += digit
        }

        return sum

}

func main() {
	var number string

	number = GetNum()

	if FirstHalfSum(number) == SecondHalfSum(number) {
		fmt.Printf("It is a lucky number!\n")
	} else {
		fmt.Printf("It isn't a lucky number!\n")
	}
}
