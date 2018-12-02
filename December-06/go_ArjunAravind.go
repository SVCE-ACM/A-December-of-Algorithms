package main

import (
        "fmt"
        "bufio"
        "os"
        "strconv"
)

/**
  * The objective of this program is to find the LCM of two given nums.
  * This can be done by using the GCD of the two numbers.
*/

func GetNum() int64 {
        fmt.Printf("Enter a number --> ")

        scanner := bufio.NewScanner(os.Stdin)
        _ = scanner.Scan()
        var enteredText string = scanner.Text()

        enteredNumber , err := strconv.ParseInt(enteredText,0,64)

        if err!=nil {
                fmt.Printf("You seem to have entered an invalid value. Try again!\n\n")
                return GetNum()
        }

        return enteredNumber
}

func MinMax (firstNum int64, secondNum int64) (int64, int64) {
	if firstNum <= secondNum {
		return firstNum, secondNum
	} else {
		return secondNum, firstNum
	}
}

func GetGCD (firstNum int64, secondNum int64) int64 {

	var smallerNum, greaterNum, iter int64
	smallerNum, greaterNum = MinMax(firstNum,secondNum)

	for iter=smallerNum; iter>0; iter-- {
		if (smallerNum%iter==0) && (greaterNum%iter==0) {
			return iter
		}
	}

	return 0 //Dummy stmt
}

func GetLCM (firstNum int64, secondNum int64) int64 {

	var smallerNum, greaterNum, gcd int64

	gcd = GetGCD(firstNum,secondNum)
	smallerNum, greaterNum = MinMax(firstNum,secondNum)

	return (greaterNum*(smallerNum/gcd))
}

func main() {

	var firstNum, secondNum int64
	firstNum = GetNum()
	secondNum = GetNum()

	fmt.Printf("The LCM of the two numbers is %v.\n", GetLCM(firstNum, secondNum))

}
