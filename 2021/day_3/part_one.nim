import strutils
import sequtils
import parseutils
import bitops

proc fromBinStringToInt(bin_string: string): int =
    var parsedNumber = 0
    let _ = parseBin(bin_string, parsedNumber)
    return parsedNumber

proc part_one() =
    let lines = readFile("input").strip.splitLines()
    let numberOfColumns = lines[0].len
    let numberOfLines = lines.len

    var numbers: seq[seq[int]] = newSeq[seq[int]](numberOfColumns).mapIt(newSeq[int](numberOfLines))

    # Fill numbers array
    for i in 0..numberOfLines - 1:
        for j in 0..numberOfColumns - 1:
            numbers[j][i] = parseInt($lines[i][j])

    # Compute gamma and epsilon
    var gammaBits: string = ""
    var epsilonBits: string = ""
    for j in 0..numberOfColumns - 1:
        let zeroes = numbers[j].count(0)
        let ones = numbers[j].count(1)
        if zeroes < ones:
            gammaBits.add("1")
            epsilonBits.add("0")
        else:
            gammaBits.add("0")
            epsilonBits.add("1")

    echo gammaBits.fromBinStringToInt() * epsilonBits.fromBinStringToInt()

part_one()
