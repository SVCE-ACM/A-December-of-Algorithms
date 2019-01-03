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

func GetArray(rows int, cols int) [][]int {
	arr := make([][]int, rows)

	for iter := 0; iter < rows; iter++ {
		arr[iter] = make([]int, cols)
	}

	return arr
}

func FillArray(arr [][]int, rows int, cols int) [][]int {

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			fmt.Printf("Enter a value for [%v][%v] --> ", i, j)
			arr[i][j] = GetValue()
		}
	}

	return arr

}

func CellIsValid(row int, col int, rows int, cols int) bool {

	if row >= 0 && row < rows {
		if col >= 0 && col < cols {
			return true
		}
	}

	return false

}

func LowerDiagonalsAreEqual(arr [][]int, rows int, cols int) bool {

	for iter := 0; iter < cols; iter++ {
		rowIter := rows;
		colIter := iter;
		val := arr[rowIter][colIter]
		for true {
			if CellIsValid(rowIter, colIter, rows, cols) {
				if val != arr[rowIter][colIter] {
					return false
				}
				rowIter--
				colIter--
			}
		}
	}

	return true

}

func FindIfDiagonalsAreEqual(arr [][]int, rows int, cols int) bool {

	if LowerDiagonalsAreEqual(arr, rows, cols) {// && UpperDiagonalsAreEqual(arr, rows, cols) {
		return true
	} else {
		return false
	}

}

func main() {

	var rows, cols int

	fmt.Printf("Enter the number of rows --> ")
	rows = GetValue()

	fmt.Printf("Enter the number of cols --> ")
	cols = GetValue()

	arr := GetArray(rows, cols)
	arr = FillArray(arr, rows, cols)

	FindIfDiagonalsAreEqual(arr, rows, cols)

}
