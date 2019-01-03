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

	/*
	  Optimised the algo here. Instead of counting back from the smallerNum
	  to 0, we keep dividing the smallerNum by 2 and check to see if it 
	  divides. However, this only goes on till it is greater than 2.
	  After that, we break the loop.
	*/

	for iter=smallerNum; iter>2; iter/=2 {
		if (smallerNum%iter==0) && (greaterNum%iter==0) {
			return iter
		}
	}

	/*
	  Let me explain this:-
	  Taking 50, the factors are 50, 25, 10, 5 and 1. Taking 234, the factors are
	  234, 117, 9, 3, 2 and 1. You will notice in all these cases that these factors
	  decrease roughly by a factor of 2. This is why the iter in the above block
	  lessens by half each time.
	*/

	/*
	  However, when sometimes, the half-point reaches 3, half of 3 is 1 and we 
	  skip over 2. This is why we break off the loop at 2 and then check manually
	  for 2 and 1.
	*/

	/*
	  By doing this, we have increased the efficiency by log(n) times where n is the 
	  magnitude of the smaller number.
	*/

	if (smallerNum%2==0) && (greaterNum%2==0) {
		return 2
	} else {
		return 1
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
