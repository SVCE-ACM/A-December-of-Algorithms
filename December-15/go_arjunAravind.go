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

func GenerateLayer(arr []int, layer int) {

	if layer == 0 {
		return
	} else if {

	}

}
