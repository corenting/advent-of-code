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
	password := 0

	for i := range lines {
		currentLine := lines[i]

		directionBytes, stepsStr := currentLine[0], currentLine[1:]
		direction := string(directionBytes)

		steps, err := strconv.Atoi(stepsStr)
		if err != nil {
			panic(err)
		}

		fmt.Printf("Currently at %d, steps is : %d\n", currentPos, steps)
		stepDir := 1
		if direction == "L" {
			stepDir = -1
		}
		currentPos = modulo(currentPos+(stepDir*steps), 100)

		if currentPos == 0 {
			password += 1
		}
	}

	fmt.Printf("Password (step 1): %d\n", password)
}
