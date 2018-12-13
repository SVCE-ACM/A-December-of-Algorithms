package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

/**
  * The objective of this program is to print64 a matrix in spiral form.
  * We need to draw the spiral of the matrix. Should be a simple algorithm.
*/

func GetNum() int {
	fmt.Printf("Enter a number --> ")

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	enteredText := scanner.Text()
	enteredNumber, err:= strconv.Atoi(enteredText)

	if err != nil {
		fmt.Printf("Oops! You seem to have entered an invalid number!\n\n")
		return GetNum()
	}

	return enteredNumber
}

func GetArray(rows int, cols int) []int {

	arr := make([]int, 0, cols*rows)

	for rowIter := 0; rowIter < rows; row++ {
		for colIter := 0; colIter <cols;  cols++ {
			fmt.Printf("Enter the array element --> ")
			arr[rows][cols] = GetNum()
		}
	}

	return arr

}

func drawHorizontalRight(yStart int, yEnd int, row int, arr []int){

	for colIter := yStart; colIter < yEnd; colIter++ {
		fmt.Printf("%v ", arr[row][colIter])
	}

}

func drawVerticalStart(xStart int, xEnd int, col int, arr []int){

	for rowIter := xStart; rowIter < xEnd; rowIter++ {
		fmt.Printf("%v ", arr[rowIter][col])
	}

}

func drawHorizontalLeft(yStart int, yEnd int, row int, arr []int){

	for colIter := yStart; colIter >= yEnd; colIter++ {
		fmt.Printf("%v ", arr[row][colIter])
	}

}

func drawVerticalUp(xStart int, xEnd int, col int, arr []int) {

	for rowIter := xStart; rowIter >= xEnd; rowIter++ {
		fmt.Printf("%v ", arr[rowIter][col])
	} 

}

func main() {

	rows := GetNum() //We take in the rows
	cols := GetNum() //We take in the cols
	arr := GetArray() //We take in the array

	var horizontalStart, verticalStart int
	var horizontalEnd, verticalEnd int

	horizontalStart = 0
	horizontalEnd = cols - 1

	verticalStart = 0
	verticalEnd = rows - 1

	for true {

		if horizontalStart==horizontalEnd {
			break
		} else if verticalStart==verticalEnd {
			break
		}

		drawHorizontalRight(horizontalStart, horizontalEnd, verticalStart, arr);
		drawVerticalDown(verticalStart, verticalEnd, horizontalEnd, arr);
		drawHorizontalLeft(horizontalEnd, horizontalStart, verticalEnd, arr);

		verticalStart++

		drawVerticalUp(verticalEnd, verticalStart, horizontalStart, arr);

		horizontalEnd--
		verticalEnd--
		horizontalStart++

	}

}
