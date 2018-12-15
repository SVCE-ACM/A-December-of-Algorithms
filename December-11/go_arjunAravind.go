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

func GetArray(rows int, cols int) [][]int {

	arr := make([][]int, 0)
	fmt.Printf("\n")

	for rowIter := 0; rowIter < rows; rowIter++ {
		arr1 := make([]int, 0)
		for colIter := 0; colIter < cols;  colIter++ {
			fmt.Printf("Enter a number for the array --> ")
			arr1 = append(arr1, GetNum())
		}
		arr = append(arr,arr1)
	}

	return arr
}

func drawHorizontalRight(yStart int, yEnd int, row int, arr [][]int){

	for colIter := yStart; colIter <= yEnd; colIter++ {
		fmt.Printf("%v ", arr[row][colIter])
	}

}

func drawVerticalDown(xStart int, xEnd int, col int, arr [][]int){

	for rowIter := xStart+1; rowIter < xEnd; rowIter++ {
		fmt.Printf("%v ", arr[rowIter][col])
	}

}

func drawHorizontalLeft(yStart int, yEnd int, row int, arr [][]int){

	for colIter := yStart; colIter >= yEnd; colIter-- {
		fmt.Printf("%v ", arr[row][colIter])
	}

}

func drawVerticalUp(xStart int, xEnd int, col int, arr [][]int) {

	for rowIter := xStart-1; rowIter > xEnd; rowIter-- {
		fmt.Printf("%v ", arr[rowIter][col])
	}

}

func main() {

	fmt.Printf("Enter the rows -> ")
	rows := GetNum() //We take in the rows

	fmt.Printf("Enter the cols -> ")
	cols := GetNum() //We take in the cols
	arr := GetArray(rows,cols) //We take in the array

	var horizontalStart, verticalStart int
	var horizontalEnd, verticalEnd int

	horizontalStart = 0
	horizontalEnd = cols - 1

	verticalStart = 0
	verticalEnd = rows - 1

	for true {

		drawHorizontalRight(horizontalStart, horizontalEnd, verticalStart, arr);

		if horizontalStart==horizontalEnd {
                        break
                } else if verticalStart==verticalEnd {
                        break
                }

		drawVerticalDown(verticalStart, verticalEnd, horizontalEnd, arr);
		drawHorizontalLeft(horizontalEnd, horizontalStart, verticalEnd, arr);

		if horizontalStart==horizontalEnd {
                        break
                } else if verticalStart==verticalEnd {
                        break
                }

		drawVerticalUp(verticalEnd, verticalStart, horizontalStart, arr);

		verticalStart++
		horizontalEnd--
		verticalEnd--
		horizontalStart++

	}

}
