package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func GetInt() int {

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	enteredNumber, _ := strconv.Atoi(scanner.Text())
	return enteredNumber

}

func IndexSums(oldArr []int, oldLength int) []int {

	if oldLength == 0 {

		arr := make([]int, 1)
		arr[0] = 1
		return arr

	} else if oldLength == 1 {

		arr := make([]int, 2)
		arr[0] = 1
		arr[1] = 1

		return arr

	} else {

		newArray := make([]int, oldLength+1)
		newArray[0] = 1
		newArray[oldLength] = 1

		newIter := 1

		for i := 0; i < oldLength-1; i++ {
			newArray[newIter] = oldArr[i] + oldArr[i+1]
			newIter++
		}

		return newArray

	}

}

func PrintNewArray(arr []int) {

	length := len(arr)

	for i := 0; i < length; i++ {
		fmt.Printf("%v ", arr[i])
	}
	fmt.Printf("\n")

}

func GenerateLayer(arr []int, layer int) {

	if layer == 0 {
		return
	} else {
		newArr := IndexSums(arr, len(arr))
		PrintNewArray(newArr)
		GenerateLayer(newArr, layer-1)
	}

}

func main() {

	fmt.Printf("Enter the number of layers that you want --> ")
	n := GetInt()

	arr := make([]int, 0)
	GenerateLayer(arr, n)

}
