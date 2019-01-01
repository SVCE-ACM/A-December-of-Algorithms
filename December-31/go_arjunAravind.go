package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

type coordinate struct {
	row int
	col int
}

func NumIsNotValid(enteredNumber int) bool {

	if enteredNumber == 1 || enteredNumber == 0 || enteredNumber == 2 {
		return false
	}

	return true

}

func GetValue() int {

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	enteredNumber, err := strconv.Atoi(scanner.Text())

	if err != nil {
		fmt.Printf("Oops! You've entered a wrong value! Try again!\n\n")
		return GetValue()
	} else if NumIsNotValid(enteredNumber) {
		fmt.Printf("oops! You've entered a wrong value! Try again!\n\n")
		return GetValue()
	}

	return enteredNumber

}

func MakeArray(rows int, cols int) [][]int {

	arr := make([][]int, rows)

	for iter := 0; iter < rows; iter++ {
		arr[iter] =  make([]int, cols)
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

func GetTwoCoordinates(arr [][]int, rows int, cols int) []coordinate {
	var twoCoordinates []coordinate

	for iter := 0; iter < rows; iter++ {
		for jiter := 0; jiter < cols; jiter++ {
			if arr[iter][jiter] == 2 {
				coord := coordinate{row: iter, col: jiter}
				twoCoordinates = append(twoCoordinates, coord)
			}
		}
	}

	return twoCoordinates
}

func GetOneCoordinate(arr [][]int, rows int, cols int) coordinate {
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if arr[i][j] == 1 {
				coords := coordinate{row: i, col: j}
				return coords
			}
		}
	}

	return coordinate{row: -1, col: -1}
}

func GetVerticalDistance(arr [][]int, rows int, cols int, twoCoords coordinate, oneCoords coordinate) int {

	directDistance := twoCoords.row - oneCoords.row

	if directDistance < 0 {
		directDistance *= -1
	}

	indirectDistance1 := (rows - oneCoords.row) + (twoCoords.row)
	indirectDistance2 := (oneCoords.row) - (rows - twoCoords.row)

	indirectDistance := 0
	if indirectDistance1 <= indirectDistance2 {
		indirectDistance = indirectDistance1
	} else {
		indirectDistance = indirectDistance2
	}

	if directDistance <= indirectDistance {
		return directDistance
	}

	return indirectDistance

}

func GetHorizontalDistance(arr [][]int, rows int, cols int, twoCoords coordinate, oneCoords coordinate) int {

	directDistance := twoCoords.col - oneCoords.col

	if directDistance < 0 {
		directDistance *= -1
	}

	indirectDistance1 := (cols - oneCoords.col) + (twoCoords.col)
	indirectDistance2 := (oneCoords.col) - (cols - twoCoords.col)

	indirectDistance := 0
	if indirectDistance <= indirectDistance2 {
		indirectDistance = indirectDistance1
	} else {
		indirectDistance = indirectDistance2
	}

	if directDistance <= indirectDistance {
		return directDistance
	}

	return indirectDistance

}

func GetDistance(arr [][]int, rows int, cols int, twoCoords coordinate) int {

	oneCoords := GetOneCoordinate(arr, rows, cols)
	verticalDistance := GetVerticalDistance(arr, rows, cols, twoCoords, oneCoords)
	horizontalDistance := GetHorizontalDistance(arr, rows, cols, twoCoords, oneCoords)

	return verticalDistance + horizontalDistance

}

func GetShortestDistanceToTwo(arr [][]int, rows int, cols int) int {

	twoCoordinates := GetTwoCoordinates(arr, rows, cols)
	shortestDistance := rows * cols

	for iter := 0; iter < len(twoCoordinates); iter++ {
		distance := GetDistance(arr, rows, cols, twoCoordinates[iter])
		if distance < shortestDistance {
			shortestDistance = distance
		}
	}

	return shortestDistance

}

func main() {

	var rows, cols int
	rows = 4
	cols = 4

	arr := MakeArray(rows, cols)
	arr = FillArray(arr, rows, cols)

	fmt.Printf("The shortest distance to 2 is %v.\n", GetShortestDistanceToTwo(arr, rows, cols))

}
