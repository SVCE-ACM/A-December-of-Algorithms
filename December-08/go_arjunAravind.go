package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	"strings"
	"regexp"
)

func IsMatch(regex string, word string) bool {
	valid, _ := regexp.MatchString(regex, word)
	return valid
}

func FindMatch(word string) int {

	if IsMatch(".*us$", word) {
		return 1 //we remove us and add -i
	} else if IsMatch(".*(is)$", word) {
		return 2 //we remove is and add -es
	} else if IsMatch(".*[(ss)(sh)(ch)sxz]$", word) {
		return 3 //we need to add -es
	} else if IsMatch(".*[f(fe)]$", word) {
		return 4 //we just need to add s
	} else if IsMatch(".*[bcdfghjklmnpqrstvwxyz]y$", word) {
		return 5 //remove y and add -ies
	} else if IsMatch(".*[aeiou]y$", word) {
		return 6 //add -s
	} else if IsMatch(".*o$", word) {
		return 7 //add -es
	} else if IsMatch(".*(on)$", word) {
		return 8 //remove on and add -a
	} else if IsMatch(".*[a-z]$", word) {
		return 9 //add -s
	} else {
		return 10 //if the word contains a number or something
	}

}

func GetPlural(word string) string {

	var str strings.Builder
	match := FindMatch(word)

	if match ==1 {
		_,_ = str.WriteString(word[:len(word)-2])
		_,_ = str.WriteString("i")
	} else if match == 2 {
		_,_ = str.WriteString(word[:len(word)-2])
		_,_ = str.WriteString("es")
	} else if match == 3 {
		_,_ = str.WriteString(word)
		_,_ = str.WriteString("es")
	} else if match == 4 {
		_,_ = str.WriteString(word)
		_,_ = str.WriteString("s")
	} else if match == 5 {
		_,_ = str.WriteString(word[:len(word)-1])
		_,_ = str.WriteString("ies")
	} else if match == 6 {
		_,_ = str.WriteString(word)
		_,_ = str.WriteString("s")
	} else if match == 7 {
		_,_ = str.WriteString(word)
		_,_ = str.WriteString("s")
	} else if match == 8 {
		_,_ = str.WriteString(word[:len(word)-2])
		_,_ = str.WriteString("a")
	} else if match == 9 {
		_,_ = str.WriteString(word)
		_,_ = str.WriteString("s")
	} else {
		_,_ = str.WriteString(word)
	}

	return str.String()

}

func GetString() string {

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	return scanner.Text()

}

func GetInt() int {

	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	enteredNumber, _ := strconv.Atoi(scanner.Text())
	return enteredNumber

}

func main() {

	fmt.Printf("Enter a word in singular form --> ")
	word := GetString()
	fmt.Printf("The plural of %v is %v.\n", word, GetPlural(word))

}
