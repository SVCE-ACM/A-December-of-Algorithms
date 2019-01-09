package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

type Coordinate struct {
	x int
	y int
}

func GetCoordinates(person string) Coordinate {
	var coord Coordinate

	//We enter the x coordinate

	fmt.Printf("Enter the x coordinate --> ")

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()
	coord.x, _ = strconv.Atoi(scanner.Text())

	//We now enter the y coordinate

	fmt.Printf("Enter the y coordinate --> ")

	_ = scanner.Scan()
	coord.y, _ = strconv.Atoi(scanner.Text())

	if (coord.y >= 0 && coord.y < 10) && (coord.x >= 0 && coord.x < 10) {
		//If theyre inside the boundaries
		if (person == "child") {

			if  (coord.y == 0 || coord.y == 9)  || (coord.x == 0 || coord.x == 9  ) {
				//Nothing happens here
			} else {
				fmt.Printf("Make sure the child is on the boundary! Try again!\n\n")
				return GetCoordinates(person)
			}

		}

	} else {
		fmt.Printf("Oops! Make sure your coords are between 0 (incl.) and 10! Try again!\n\n")
		return GetCoordinates(person)
	}

	return coord

}

func FindRoute(santa Coordinate, child Coordinate) {

	//We first make sure the x coordinate is matching with the child coordinate
	for true {

		fmt.Printf("Santa is at (%v,%v).\n", santa.x, santa.y)

		if santa.x < child.x {
			santa.x++
		} else if santa.x > child.x {
			santa.x--
		} else {
			break;
		}

	}

	//We now make sure the y coordinate is matching with the child coordinate
	for true {

		fmt.Printf("Santa is at (%v,%v).\n", santa.x, santa.y)

		if (santa.y < child.y) {
			santa.y++
		} else if santa.y > child.y {
			santa.y--
		} else {
			fmt.Printf("Santa has arrived! Merry Christmas!\n\n")
			break;
		}

	}

}

func main() {

	var santa, child Coordinate

	fmt.Printf("\nEnter the coordinates of Santa :=\n")
	santa = GetCoordinates("santa")

	fmt.Printf("\nEnter the coordinates of the child :=\n")
	child = GetCoordinates("child")

	fmt.Printf("\n")
	FindRoute(santa, child)
}
