import strutils
import sequtils
import parseutils
import bitops

proc fromBinStringToInt(bin_string: string): int =
    var parsedNumber = 0
    let _ = parseBin(bin_string, parsedNumber)
    return parsedNumber

proc computeRating(initialLines: seq[string], deletionRule: proc(numberOfZeroes: int, numberOfOnes: int): int): int =
    var lines = deepCopy(initialLines)
    let numberOfBits = lines[0].len

    for i in 0..numberOfBits:

        # If last one, it's the result
        if lines.len == 1:
            return lines[0].fromBinStringToInt()

        var currentPositionValues: seq[int]
        for j in 0..lines.len - 1:
            currentPositionValues.add(parseInt($lines[j][i]))

        let numberOfZeroes = currentPositionValues.count(0)
        let numberOfOnes = currentPositionValues.count(1)
        let numberToDelete = deletionRule(numberOfZeroes, numberOfOnes)

        lines.keepItIf(parseInt($it[i]) != numberToDelete)

proc oxygenRatingRules(numberOfZeroes: int, numberOfOnes: int): int =
    if numberOfOnes < numberOfZeroes:
        return 1
    else:
        return 0

proc co2ScrubberRating(numberOfZeroes: int, numberOfOnes: int): int =
    if numberOfOnes < numberOfZeroes:
        return 0
    else:
        return 1


proc part_two() =
    let lines = readFile("input").strip.splitLines()

    let oxygenRating = computeRating(lines, oxygenRatingRules)
    let co2ScrubberRating = computeRating(lines, co2ScrubberRating)

    echo oxygenRating * co2ScrubberRating

part_two()
