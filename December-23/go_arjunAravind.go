package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

type section struct {
	name string
	strength int
}

type classroom struct {
	capacity int
}

/* Struct functions start here */
func InitClassrooms(number int, capacit int) classroom {

	return classroom{capacity=capacit}

}

func InitSections() []section {

	fmt.Printf("\nEnter the number of departments --> ")
	depNum := GetInt()

	sections := make([]section, depNum)

	fmt.Printf("\n")
	for iter := 0; iter < depNum; iter++ {
		fmt.Printf("Enter the name of the dept --> ")
		sections[iter].name = GetString()

		fmt.Printf("Enter the strength of the dept --> ")
		sections[iter].strength = GetInt()
		fmt.Printf("\n")
	}

	return sections

}

/* Program Functions Start Here */
func GetInt() int {

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	enteredNumber, _ := strconv.Atoi(scanner.Text())
	return enteredNumber

}

func GetString() string {

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	return scanner.Text()

}

func CalculateExamSeating(classrooms classroom, sections []section) {

	classroomIter := 1
	columnIter := 1

	sectionNum := len(sections) //number of sections
	sectionIter := 1 //for iterating the sections
	studentIter := make([]int, sectionIter) //for counting students in each dept

	studentCount := 0 //for coutning number of students in classroom

	for iter := 0; iter < sectionIter; iter++ {
		studentIter[iter] = 1
	}

	columns = len(sections) + 1

	for true {

		fmt.Printf("ROOM %v\n", classroomIter)

		for true {

			if columnIter == 4 {
				fmt.Printf("\n")
				columnIter = 1
			}

			if studentCount >= classrooms.capacity {
				break
			}

			fmt.Printf("%v%v ", sections[sectionIter].name, studentIter[sectionIter]

			studentIter[sectionIter]++
			columnIter++

		}

	}

}

/* Main method starts here */
func main() {

	fmt.Printf("Enter the capacity of each classroom --> ")
	classroomCap := GetInt()

	classrooms := InitClassrooms(classroomCap)
	sections := InitSections()

	CalculateExamSeating(classrooms, sections)

}
