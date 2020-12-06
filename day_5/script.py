def parse_bounds(low, high, item, max_value):
    serie = range(max_value + 1)
    for char in item:
        middle = len(serie) // 2
        if char == low:
            serie = serie[:middle]
        elif char == high:
            serie = serie[middle:]
        else:
            raise Exception("Invalid char")

        if len(serie) == 1:
            return serie[0]

    raise Exception("Should not end here")


lines = []
with open('input', 'r') as input_file:
    for line in input_file:
        lines.append(line.strip())

max_seat_id = -1
for item in lines:
    row = parse_bounds("F", "B", item[:7], 127)
    column = parse_bounds("L", "R", item[-3:], 7)
    seat_id = row * 8 + column
    max_seat_id = max(seat_id, max_seat_id)

print(f"Max seat id: {max_seat_id}")
