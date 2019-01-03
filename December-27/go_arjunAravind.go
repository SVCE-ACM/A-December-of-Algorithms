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

func GetChar() byte {
	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	return scanner.Text()[0]
}

func GetArray(rows int, cols int) [][]byte {

	arr := make([][]byte, rows)

	for i := 0; i < rows; i++ {
		arr[i] = make([]byte, cols)
	}

	return arr

}

func CharIsVowel(character byte) bool {

	switch character {
		case 'a':
			return true
		case 'e':
			return true
		case 'o':
			return true
		case 'i':
			return true
		case 'u':
			return true
		case 'A':
			return true
		case 'E':
			return true
		case 'I':
			return true
		case 'O':
			return true
		case 'U':
			return true
		default:
			return false;
	}

}

func SquareIsValid(arr [][]byte, row int, col int) bool {

	if CharIsVowel(arr[row][col]) {
		if  CharIsVowel(arr[row+1][col]) {
			if CharIsVowel(arr[row+1][col+1]) {
				if CharIsVowel(arr[row][col+1]) {
					return true
				}
			}
		}
	}

	return false

}

func FillArray(arr [][]byte, rows int, cols int) [][]byte {

	fmt.Printf("\n")
	for i := 0; i < rows; i++ {
		for j := 0; j < cols;  j++ {
			fmt.Printf("Enter a value for [%v][%v] --> ", i, j)
			arr[i][j] = GetChar()
		}
	}

	return arr
}

func FindSquare(arr [][]byte, rows int, cols int) {

	for i := 0; i < rows-1; i++ {
		for j := 0; j < cols-1; j++ {
			if SquareIsValid(arr, i, j) {
				fmt.Printf("It is available! Starts at [%v][%v].\n\n", i, j)
				return;
			}
		}
	}

	fmt.Printf("The square doesn't exist!\n\n")

}

func main() {

	var rows, cols int

	fmt.Printf("Enter the number of rows --> ")
	rows = GetValue()

	fmt.Printf("Enter the number of cols --> ")
	cols = GetValue()

	arr := GetArray(rows, cols)
	arr = FillArray(arr, rows, cols)

	FindSquare(arr, rows, cols)

}
