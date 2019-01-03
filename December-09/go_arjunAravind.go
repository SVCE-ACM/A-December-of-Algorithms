package main

import (
	"fmt"
	"bufio"
	"os"
)

/**
  * Implemented this URL checking algorithm using DFA-like concepts.
  * Every character causes a state change based on the transition function. 
 */

type State struct {
	CurrentState int8
	finalState int8
}

func newState () State {
	var state State
	state.CurrentState = 0
	state.finalState = 7

	return state
}

func getState (state State, character string) int8 {

	//fmt.Printf("character here is %v\n", character)

	if state.CurrentState == 0 {

		if isAlphabet(character) {
			state.CurrentState = 1
		} else {
			state.CurrentState = -1
		}

	} else if state.CurrentState == 1 {

		if isAlphabet(character) {
			state.CurrentState = 1
		} else if isColon(character) {
			state.CurrentState = 2
		} else {
			state.CurrentState = -1
		}

	} else if state.CurrentState == 2 {

		if isSlash(character) {
			state.CurrentState = 3
		} else {
			state.CurrentState = -1
		}

	} else if state.CurrentState == 3 {

		if isSlash(character) {
			state.CurrentState = 4
		} else {
			state.CurrentState = -1
		}

	} else if state.CurrentState == 4 {

		if isAlphabet(character) {
			state.CurrentState = 5
		} else {
			state.CurrentState = -1
		}

	} else if state.CurrentState == 5 {

		if isAlphabet(character) {
			state.CurrentState = 5
		} else if isDigit(character) {
			state.CurrentState = 5
		} else if isOtherValid(character) {
			state.CurrentState = 5
		} else if isDot(character) {
			state.CurrentState = 6
		} else {
			state.CurrentState = -1
		}

	} else if state.CurrentState == 6 {

		if isAlphabet(character) {
			state.CurrentState = 7
		} else {
			state.CurrentState = -1
		}

	} else if state.CurrentState == 7 {

		if isAlphabet(character) || isDigit(character) {
			state.CurrentState = 7
		} else if isOtherValid(character) {
			state.CurrentState = 7
		} else if isDot(character) {
			state.CurrentState = 6
		} else if isSlash(character) {
			state.CurrentState = 8
		} else {
			state.CurrentState = -1
		}

	} else if state.CurrentState == 8 {

		if isAlphabet(character) {
			state.CurrentState = 7
		} else if isSlash(character) {
			state.CurrentState = 7
		} else {
			state.CurrentState = -1
		}

	}

	return state.CurrentState

}

func inFinalState (state State) bool {

	if state.CurrentState == 7 || state.CurrentState == 8 {
		return true
	} else {
		return false
	}

}

func isAlphabet (letter string) bool {
	character := []rune(letter)[0]

	if (character >= 97) && (character <= 122) {
		return true
	} else if (character >= 65) && (character <= 90) {
		return true
	} else {
		return false
	}
}

func isDigit (digit string) bool {
	character := []rune(digit)[0]

	if (character >= 48) && (character <= 57) {
		return true
	} else {
		return false
	}
}

func isDot (dot string) bool {
	character := []rune(dot)[0]

	if character == 46 {
		return true
	} else {
		return false
	}
}

func isSlash (slash string) bool {
	character := []rune(slash)[0]

	if character == 47 {
		return true
	} else {
		return false
	}
}

func isColon (colon string) bool {
	character := []rune(colon)[0]

	if character == 58 {
		return true
	} else {
		return false
	}
}

func isOtherValid (other string) bool {
	character := []rune(other)[0]

	if character == 45 || character == 95 {
		return true
	} else {
		return false
	}
}

func getURL() string {

	fmt.Printf("Enter a URL --> ")

        scanner := bufio.NewScanner(os.Stdin)
        _ = scanner.Scan()

        var enteredText string = scanner.Text()
        return enteredText

}

func main () {

	word := getURL()
	length := len(word)
	i := length

	state := newState()

	for i = 0; i < length; i++ {
		state.CurrentState = getState(state, string(word[i]))

		//fmt.Printf("%v and %v and %v\n", string(word[i]), word[i], state.CurrentState)
	}

	if inFinalState(state) {
		fmt.Printf("It is valid!\n")
	} else {
		fmt.Printf("It is not valid!\n")
	}

}
