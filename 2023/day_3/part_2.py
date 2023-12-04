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

def has_a_symbol_neighbor(lines, index, digit_position, is_start, is_end) -> tuple[bool, tuple[int, int] | None]:
    """
    Get the symbol neighbor and return the position of it.
    """
    vertical_positions = [index - 1, index, index + 1]
    horizontal_positions = [digit_position - 1, digit_position, digit_position + 1]

    if is_start and neighbor_is_symbol(lines, index, digit_position - 1):
        return True, (index, digit_position - 1)
    if is_end and neighbor_is_symbol(lines, index, digit_position + 1):
        return True, (index, digit_position + 1)

    for vertical_pos, horizontal_pos in itertools.product(vertical_positions, horizontal_positions):
        if neighbor_is_symbol(lines, vertical_pos, horizontal_pos):
            return True, (vertical_pos, horizontal_pos)

    return False, None

lines = get_lines()

i = 0
symbols_and_numbers = {}
for line in lines:
    matches = NUM_REGEX.finditer(line)
    for regex_match in matches:
        number = int(regex_match.group())
        start, end = regex_match.span()
        end -= 1 # span() return the next character for end

        for digit_position in list(range(start, end + 1)):
            has_symbol, symbol_pos_tuple = has_a_symbol_neighbor(lines, i, digit_position, digit_position == start, digit_position == end)

            if has_symbol:
                # add current line to the tuple: the position is line + vertical + horizontal position
                if symbol_pos_tuple in symbols_and_numbers:
                    symbols_and_numbers[symbol_pos_tuple].append(number)
                else:
                    symbols_and_numbers[symbol_pos_tuple] = [number]
                break
    i += 1

gears_sum = 0
for symbol, numbers in symbols_and_numbers.items():
    if len(numbers) == 2:
        gears_sum += numbers[0] * numbers[1]

print(f"Part 2: {gears_sum}")
