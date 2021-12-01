from enum import Enum
from dataclasses import dataclass

class Operand(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    LEFT = "L"
    RIGHT = "R"
    FORWARD = "F"

class Direction(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"

    def get_index(self):
        indexes = {
            Direction.NORTH: 0,
            Direction.EAST: 1,
            Direction.SOUTH: 2,
            Direction.WEST: 3,
        }
        return indexes[self]

@dataclass
class Instruction:
    operand: Operand
    argument: int

class Machine:
    def __init__(self, instructions):
        self.instructions = instructions
        self.direction = Direction.EAST
        self.east_position = 0
        self.north_position = 0

        self.instruction_index = 0

    def execute(self):
        while self.instruction_index < len(self.instructions):
            instruction = self.instructions[self.instruction_index]
            method_name = str(instruction.operand).split('.')[1].lower()
            getattr(self, method_name)(instruction.argument)
            self.instruction_index += 1

    def north(self, argument):
        self.north_position += argument

    def south(self, argument):
        self.north_position -= argument

    def east(self, argument):
        self.east_position += argument

    def west(self, argument):
        self.east_position -= argument

    def forward(self, argument):
        direction_name = str(self.direction).split('.')[1].lower()
        getattr(self, direction_name)(argument)

    def right(self, argument):
        self.turn(argument)

    def left(self, argument):
        self.turn(-argument)

    def turn(self, argument):
        move = argument / 90
        current_direction_index = self.direction.get_index()
        new_index = (current_direction_index + move) % 4

        for direction in Direction:
            if direction.get_index() == new_index:
                self.direction = direction
                return

    def get_manhattan_distance(self):
        return abs(self.east_position) + abs(self.north_position)

def get_lines():
    lines = []
    with open('input', 'r') as input_file:
        for line in input_file:
            lines.append(line.strip())
    return lines

def parse_instructions(lines):
    for line in lines:
        yield Instruction(
            operand=Operand(line[0]),
            argument=int(line[1:])
        )

def part_1():
    lines = get_lines()
    instructions = parse_instructions(lines)

    machine = Machine(list(instructions))
    machine.execute()
    print(f"Part 1: {machine.direction}, {machine.get_manhattan_distance()}")


if __name__ == "__main__":
    part_1()
