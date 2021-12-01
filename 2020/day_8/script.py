from enum import Enum
from dataclasses import dataclass

class Operand(Enum):
    ACC = "acc"
    JMP = "jmp"
    NOP = "nop"

@dataclass
class Instruction:
    operand: Operand
    argument: int

class Machine:
    def __init__(self, instructions):
        self.instructions = instructions
        self.executions_count = [0 for i in range(len(instructions))]
        self.accumulator = 0
        self.position = 0

    def execute(self):
        while True:
            if self.executions_count[self.position] > 1:
                return False

            instruction = self.instructions[self.position]
            getattr(self, instruction.operand.value)(instruction.argument)

            if self.position >= len(self.instructions):
                return True

            self.executions_count[self.position] += 1


    def nop(self, _):
        self.position += 1

    def acc(self, argument):
        self.accumulator += argument
        self.position += 1

    def jmp(self, argument):
        self.position += argument


def get_lines():
    lines = []
    with open('input', 'r') as input_file:
        for line in input_file:
            lines.append(line.strip())
    return lines

def parse_instructions(lines):
    for line in lines:
        splitted = line.split(' ')
        yield Instruction(
            operand=Operand(splitted[0].strip()),
            argument=int(splitted[1])
        )


def part_1():
    lines = get_lines()
    instructions = parse_instructions(lines)

    machine = Machine(list(instructions))
    machine.execute()
    print(f"Accumulator: {machine.accumulator}")

def part_2():
    lines = get_lines()
    instructions = list(parse_instructions(lines))

    permutations = []
    for i in range(len(instructions)):
        original_instruction = instructions[i]

        if original_instruction.operand in [Operand.JMP, Operand.NOP]:
            new_instruction = Instruction(
                operand=Operand.NOP if original_instruction.operand == Operand.JMP else Operand.JMP,
                argument=original_instruction.argument
            )
            permutations.append(
                instructions[:i] + [new_instruction] + instructions[i+1:]
            )

    for permutation in permutations:
        machine = Machine(permutation)
        ret = machine.execute()
        if ret:
            print(f"Accumulator: {machine.accumulator}")
            break

if __name__ == "__main__":
    part_1()
    part_2()
