package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func getInputLines() []string {
	bytesRead, err := os.ReadFile("input")
	if err != nil {
		panic("cannot read input")
	}
	fileContent := string(bytesRead)
	ret := slices.DeleteFunc(strings.Split(fileContent, "\n"), func(line string) bool {
		return line == ""
	})
	return ret
}

func modulo(a int, b int) int {
	c := a % b
	if c < 0 {
		return c + b
	} else {
		return c
	}
}

func main() {
	lines := getInputLines()
	currentPos := 50
	passwordStep1 := 0
	passwordStep2 := 0

	for i := range lines {
		currentLine := lines[i]

		directionBytes, stepsStr := currentLine[0], currentLine[1:]
		direction := string(directionBytes)

		steps, err := strconv.Atoi(stepsStr)
		if err != nil {
			panic(err)
		}

		stepDir := 1
		numberOfZeroEncounters := 0
		// For the left
		if direction == "L" {
			stepDir = -1

			if steps >= currentPos {
				if currentPos != 0 {
					numberOfZeroEncounters = ((steps - currentPos) / 100) + 1
				} else {
					numberOfZeroEncounters = ((steps - currentPos) / 100)
				}
			}
		} else {
			numberOfZeroEncounters = ((currentPos + steps) / 100)
		}
		currentPos = modulo(currentPos+(stepDir*steps), 100)

		// Compute password for step 1
		if currentPos == 0 {
			passwordStep1 += 1
		}

		// Check for wrapping for part 2
		if numberOfZeroEncounters > 0 {
			passwordStep2 += numberOfZeroEncounters
		}
	}

	fmt.Printf("Password (step 1): %d\n", passwordStep1)
	fmt.Printf("Password (step 2): %d\n", passwordStep2)
}
