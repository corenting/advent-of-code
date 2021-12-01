import strutils
import sequtils

proc main() =
    let numbers = readFile("input").strip.splitLines().mapIt(parseInt(it))
    let sums = zip(zip(numbers, numbers[1..^1]), numbers[2..^1]).mapIt((it[0][0] + it[0][1] + it[1]))

    echo filter(zip(sums, sums[1..^1]), proc(x: (int, int)): bool = x[1] > x[0]).len

main()
