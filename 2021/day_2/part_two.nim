import strutils
import sequtils

type
  InstructionType = enum
    forward = "forward", up = "up", down = "down"

type
  Position = object
    horizontal: int
    depth: int
    aim: int

type
  Instruction = object
    instruction_type: InstructionType
    amount: int

proc translateInstruction(command_string: string): Instruction =
    let splittedString = command_string.split(" ")
    return Instruction(
        instruction_type: parseEnum[InstructionType](splittedString[0]),
        amount: parseINt(splittedString[1])
    )

proc part_two() =
    let instructions = readFile("input").strip.splitLines().mapIt(translateInstruction(it))
    var position = Position(horizontal: 0, depth: 0)

    for instruction in instructions:
        case instruction.instruction_type:
            of InstructionType.forward:
                position.horizontal += instruction.amount
                position.depth += position.aim * instruction.amount
            of InstructionType.up:
                position.aim -= instruction.amount
            of InstructionType.down:
                position.aim +=  instruction.amount

    echo position.horizontal * position.depth

part_two()
