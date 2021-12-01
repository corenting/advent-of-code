import strutils
import sequtils

proc main() =
    let numbers = readFile("input").strip.splitLines().mapIt(parseInt(it))
    echo filter(zip(numbers, numbers[1..^1]), proc(x: (int, int)): bool = x[1] > x[0]).len

main()
