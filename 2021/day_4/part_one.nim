import strutils
import sequtils
import parseutils
import bitops

type
  BoardItem = object
    value: int
    drawn: bool

proc parseBoards(lines: seq[string]):seq[seq[seq[BoardItem]]] =
  var res: seq[seq[seq[BoardItem]]] = @[]

  var currentBoard:seq[seq[BoardItem]] = @[]
  for i in 0..lines.len - 1:

    # Empty line means new board
    if isEmptyOrWhitespace(lines[i]):
      res.add(currentBoard)
      currentBoard = @[]
      continue

    currentBoard.add(
      lines[i]
        .split(" ")
        .filterIt(not isEmptyOrWhitespace(it))
        .mapIt(BoardItem(value: parseInt(it), drawn: false))
    )

  res.add(currentBoard)  # don't forget the last board

  return res

proc boardHasWon(board: seq[seq[BoardItem]]):bool =
  # Check for lines
  let lineLength = board[0].len
  for line in board:
    if line.filterIt(it.drawn).len == lineLength:
      return true

  # Check for columns
  let columnLength = board.len
  for column in 0..columnLength - 1:
    var currentColumn: seq[BoardItem] = @[]

    for line in board:
      currentColumn.add(line[column])

    if currentColumn.filterIt(it.drawn).len == columnLength:
      return true

  return false

proc computeScore(board: seq[seq[BoardItem]], lastNumber: int): int =
  var notDrawn: seq[int] = @[]
  for line in board:
    notDrawn.add(line.filterIt(not it.drawn).mapIt(it.value))

  return foldl(notDrawn, a + b) * lastNumber

proc partOne() =
    let fileLines = readFile("input").strip.splitLines()
    let drawnNumbers = fileLines[0].split(',').mapIt(parseInt(it))
    var boards = parseBoards(fileLines[2..^1])

    # Game loop (with .mitems to modify items in-place)
    for number in drawnNumbers:
      for board in boards.mitems:
        for line in board.mitems:
          for item in line.mitems:
            if item.value == number:
              item.drawn = true

        if boardHasWon(board):
          echo computeScore(board, number)
          return

partOne()
