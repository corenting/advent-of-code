import nre
import strutils
import sequtils

type
  Item = object
    letter: char
    min: int
    max: int
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
                min:parseInt(regex.captures[0]),
                max:parseInt(regex.captures[1]),
                password:regex.captures[3],
            )

            let letterCount = item.password.countIt(it == item.letter)
            if letterCount >= item.min and letterCount <= item.max:
                valid += 1

        except EOFError:
            break
    echo valid


main()
