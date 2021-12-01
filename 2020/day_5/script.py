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


def get_seat_id(row, column):
    return row * 8 + column

lines = []
with open('input', 'r') as input_file:
    for line in input_file:
        lines.append(line.strip())

max_seat_id = -1
rows = {
    i: [] for i in range(127 + 1)
}
all_seats_ids = []
for item in lines:
    row = parse_bounds("F", "B", item[:7], 127)
    column = parse_bounds("L", "R", item[-3:], 7)
    seat_id = get_seat_id(row, column)
    all_seats_ids.append(seat_id)
    max_seat_id = max(seat_id, max_seat_id)
    rows[row].append(column)

print(f"Max seat id: {max_seat_id}")

missing_seat_ids = []
for key, row in rows.items():
    all_rows = [i for i in range(7 + 1)]
    missing = set(all_rows) - set(row)
    if len(missing) > 0:
        for num in missing:
            missing_seat_ids.append(get_seat_id(key, num))

for seat_id in missing_seat_ids:
    if seat_id - 1 in all_seats_ids and seat_id + 1 in all_seats_ids:
        print(f"My seat ID is: {seat_id}")
        break
