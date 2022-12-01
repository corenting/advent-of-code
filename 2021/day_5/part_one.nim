import strutils
import sequtils
import std/tables
import std/hashes

type
  Position = object
    horizontal: int
    vertical: int

proc hash(x: Position): Hash =
    return x.vertical.hash !& x.horizontal.hash

proc mapInstruction(instruction: string): (Position, Position) =
    let textPositions = instruction.split("->").mapIt(strip(it))

    let startPosition = textPositions[0].split(",").mapIt(parseInt(it))
    let endPosition = textPositions[1].split(",").mapIt(parseInt(it))

    return (
        Position(horizontal: startPosition[0], vertical: startPosition[1]),
        Position(horizontal: endPosition[0], vertical: endPosition[1]),
    )

proc generateCoveredPositions(startPosition: Position, endPosition: Position): seq[Position] =
    # Horizontal lines then vertical lines case
    # TODO: handle other order (bigger position first)
    var retValues: seq[Position] = @[]
    if startPosition.horizontal == endPosition.horizontal:
        for i in startPosition.vertical..endPosition.vertical:
            retValues.add(Position(horizontal: startPosition.horizontal, vertical: i))
    elif startPosition.vertical == endPosition.vertical:
        for i in startPosition.horizontal..endPosition.horizontal:
            retValues.add(Position(horizontal: i, vertical: startPosition.vertical))
    return retValues

proc partOne() =
    let startAndEndPositions = readFile("input").strip.splitLines().mapIt(mapInstruction(it))

    var coveredPositions = newTable[Position, int]()
    for item in startAndEndPositions:
        let newPositions = generateCoveredPositions(item[0], item[1])
        echo(newPositions)
        for position in newPositions:
            var existingCount = coveredPositions.getOrDefault(position)
            coveredPositions[position] = existingCount + 1

    # Compute points with two or more lines
    var finalCount = 0
    for v in coveredPositions.values:
        if v > 1:
            finalCount += 1

    echo(finalCount)

partOne()
