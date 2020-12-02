import nre
import strutils

type
  Item = object
    letter: char
    firstPos: int
    secondPos: int
    password: string

proc main() =
    let f = open("input")
    defer: f.close()

    var valid = 0
    while true:
        var line: string
        try:

            line = f.readLine()
            var regex = line.match(re"(\d+)-(\d+) ([a-z]): ([a-z]+)").get()
            let item = Item(
                letter:regex.captures[2][0],
                firstPos:parseInt(regex.captures[0]) - 1,
                secondPos:parseInt(regex.captures[1]) - 1,
                password:regex.captures[3],
            )

            if (item.password[item.firstPos] == item.letter and item.password[item.secondPos] != item.letter) or (item.password[item.secondPos] == item.letter and item.password[item.firstPos] != item.letter):
                valid += 1

        except EOFError:
            break
    echo valid


main()
