import itertools
import re

NUM_REGEX = re.compile(r"(\d+)")
NOT_SYMBOLS = [str(i) for i in range(0, 10)] + ["."]

def get_lines() -> list[str]:
    lines = []
    with open('input', 'r') as input_file:
        for line in input_file:
            if stripped_line := line.strip():
                lines.append(stripped_line)
    return lines

def neighbor_is_symbol(lines, vertical_position, horizontal_position) -> bool:
    try:
        if lines[vertical_position][horizontal_position] not in NOT_SYMBOLS:
            return True
        return False
    except IndexError:
        return False

def has_a_symbol_neighbor(lines, index, digit_position, is_start, is_end) -> bool:
    vertical_positions = [index - 1, index, index + 1]
    horizontal_positions = [digit_position - 1, digit_position, digit_position + 1]

    if is_start and neighbor_is_symbol(lines, index, digit_position - 1):
        return True
    if is_end and neighbor_is_symbol(lines, index, digit_position + 1):
        return True

    for vertical_pos, horizontal_pos in itertools.product(vertical_positions, horizontal_positions):
        if neighbor_is_symbol(lines, vertical_pos, horizontal_pos):
            return True

    return False

lines = get_lines()

i = 0
sum = 0
for line in lines:
    matches = NUM_REGEX.finditer(line)
    for regex_match in matches:
        number = int(regex_match.group())
        start, end = regex_match.span()
        end -= 1 # span() return the next character for end
        is_valid_part = False

        for digit_position in list(range(start, end + 1)):
            if has_a_symbol_neighbor(lines, i, digit_position, digit_position == start, digit_position == end):
                is_valid_part = True
                break

        if is_valid_part:
            sum += number
    i += 1

print(f"Part 1: {sum = }\n")
