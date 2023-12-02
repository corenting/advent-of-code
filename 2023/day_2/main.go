package main

import (
	"fmt"
	"os"
	"regexp"
	"slices"
	"strconv"
	"strings"
)

type gameTurn struct {
	redCount   int
	blueCount  int
	greenCount int
}

type game struct {
	id    int
	turns []gameTurn
}

var gameIdRegex = regexp.MustCompile(`Game ([0-9]+): `)

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

func getGameId(line string) int {
	gameIdMatch, err := strconv.Atoi(gameIdRegex.FindStringSubmatch(line)[1])
	if err != nil {
		panic("cannot parse game id")
	}
	return gameIdMatch
}

func getTurns(line string) []gameTurn {
	turnsAsText := gameIdRegex.ReplaceAllString(line, "")
	turnsArray := strings.Split(turnsAsText, ";")

	redRegex := regexp.MustCompile(`([0-9]+) red`)
	blueRegex := regexp.MustCompile(`([0-9]+) blue`)
	greenRegex := regexp.MustCompile(`([0-9]+) green`)
	turns := make([]gameTurn, 0, 10)
	for i := 0; i < len(turnsArray); i++ {
		redCount := 0
		blueCount := 0
		greenCount := 0

		redMatch := redRegex.FindStringSubmatch(turnsArray[i])
		if redMatch != nil {
			redCount, _ = strconv.Atoi(redMatch[1])
		}

		blueMatch := blueRegex.FindStringSubmatch(turnsArray[i])
		if blueMatch != nil {
			blueCount, _ = strconv.Atoi(blueMatch[1])
		}

		greenMatch := greenRegex.FindStringSubmatch(turnsArray[i])
		if greenMatch != nil {
			greenCount, _ = strconv.Atoi(greenMatch[1])
		}

		turns = append(turns, gameTurn{
			redCount:   redCount,
			blueCount:  blueCount,
			greenCount: greenCount,
		})
	}

	return turns
}

func main() {
	lines := getInputLines()

	// Parse input
	games := make([]game, 0, 100)
	for i := 0; i < len(lines); i++ {
		var currentGame game
		currentGame.id = getGameId(lines[i])
		currentGame.turns = getTurns(lines[i])
		games = append(games, currentGame)
	}

	// Part 1
	maxRed := 12
	maxBlue := 14
	maxGreen := 13
	possibleGamesIdsSum := 0
	for i := 0; i < len(games); i++ {
		currentGame := games[i]
		gameIsPossible := true
		for j := 0; j < len(currentGame.turns); j++ {
			currentTurn := currentGame.turns[j]
			if currentTurn.redCount > maxRed || currentTurn.blueCount > maxBlue || currentTurn.greenCount > maxGreen {
				gameIsPossible = false
				break
			}
		}

		if gameIsPossible {
			fmt.Printf("Game %d is possible\n", currentGame.id)
			possibleGamesIdsSum += currentGame.id
		} else {
			fmt.Printf("Game %d is not possible\n", currentGame.id)
		}
	}
	fmt.Printf("Part 1: %d\n\n", possibleGamesIdsSum)

	// Part 2
	powerSum := 0
	for i := 0; i < len(games); i++ {
		currentGame := games[i]
		minRed := 0
		minBlue := 0
		minGreen := 0

		for j := 0; j < len(currentGame.turns); j++ {
			currentTurn := currentGame.turns[j]
			minRed = max(minRed, currentTurn.redCount)
			minBlue = max(minBlue, currentTurn.blueCount)
			minGreen = max(minGreen, currentTurn.greenCount)
		}

		fmt.Printf("Game %d can be played with %d red, %d blue and %d green \n", currentGame.id, minRed, minBlue, minGreen)
		gamePower := minRed * minBlue * minGreen
		fmt.Printf("    Power of %d\n", gamePower)
		powerSum += gamePower
	}
	fmt.Printf("Part 2: %d\n", powerSum)

}
