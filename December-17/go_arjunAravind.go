package main

import "fmt"

func GetArray(side int) [][]int {

	arr := make([][]int, side)

	for i := 0; i < side; i++ {
		arr[i] = make([]int, side)
	}

	for i := 0; i < side; i++ {
		for j := 0; j < side; j++ {
			arr[i][j] = 0
		}
	}

	return arr

}

func GetMagicConstant(side int) int {
	return (side * ((side*side) + 1)) / 2
}

type threeNums struct {
	num1 int
	num2 int
	num3 int
}

func GenerateSumNums(sum int, max int) []threeNums {

	threeArray := make([]threeNums, (side+side+2))
	threeArrayIter := 0

	for i := 1; i < max; i++ {
		for j := 1; j < max; j++ {
			for k := 1; k < max; k++ {
				if (i + j + k) == sum {
					threeArray[threeArrayIter] = threeNums{num1: i, num2: j, num3: k}
					threeArrayIter++
				}
			}
		}
	}

	return threeArray

}

func main() {

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	enteredNumber, _ = strconv.Atoi(scanner.Text())

	GenerateSumNums(enteredNumber)

}
