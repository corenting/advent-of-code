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


ROTATION_MATRIX = {
    Operand.LEFT: {
        90: [
            [0, -1],
            [1, 0],
        ],
        180: [
            [-1, 0],
            [0, -1],
        ],
        270: [
            [0, 1],
            [-1, 0],
        ],
    },
    Operand.RIGHT: {
        90: [
            [0, 1],
            [-1, 0],
        ],
        180: [
            [-1, 0],
            [0, -1],
        ],
        270: [
            [0, -1],
            [1, 0],
        ],
    }
}

@dataclass
class Instruction:
    operand: Operand
    argument: int

class Machine:
    def __init__(self, instructions):
        self.instructions = instructions
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.instruction_index = 0

    def execute(self):
        while self.instruction_index < len(self.instructions):
            instruction = self.instructions[self.instruction_index]
            method_name = str(instruction.operand).split('.')[1].lower()
            getattr(self, method_name)(instruction.argument)
            self.instruction_index += 1

    def north(self, argument):
        self.waypoint_y += argument

    def south(self, argument):
        self.waypoint_y -= argument

    def east(self, argument):
        self.waypoint_x += argument

    def west(self, argument):
        self.waypoint_x -= argument

    def forward(self, argument):
        self.x += self.waypoint_x * argument
        self.y += self.waypoint_y * argument

    def right(self, argument):
        self.move_waypoint(Operand.RIGHT, argument)

    def left(self, argument):
        self.move_waypoint(Operand.LEFT, argument)

    def move_waypoint(self, operand, argument):
        rotation = ROTATION_MATRIX[operand][argument]
        tmp_x = self.waypoint_x
        tmp_y = self.waypoint_y
        self.waypoint_x = tmp_x * rotation[0][0] +  tmp_y * rotation[0][1]
        self.waypoint_y = tmp_x * rotation[1][0] + tmp_y * rotation[1][1]

    def get_manhattan_distance(self):
        return abs(self.x) + abs(self.y)

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

def part_2():
    lines = get_lines()
    instructions = parse_instructions(lines)

    machine = Machine(list(instructions))
    machine.execute()
    print(f"Part 2: {machine.get_manhattan_distance()}")

if __name__ == "__main__":
    part_2()
