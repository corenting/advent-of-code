
def get_lines():
    lines = []
    with open('input', 'r') as input_file:
        for line in input_file:
            lines.append(line.strip())
    return lines


def part_1():
    lines = get_lines()
    start_time = int(lines[0])
    bus_list = [int(line) for line in lines[1].split(',') if line != "x"]
    max_time = start_time + 100

    schedule = {}
    for i in range(start_time, max_time):
        lines_at_time = [line for line in bus_list if i % line == 0]
        if len(lines_at_time) > 0:
            schedule[i] = lines_at_time

    # Get earliest one
    time, lines = list(schedule.items())[0]
    waiting_time = time - start_time
    print(f"Part 1: Line {lines[0]}, waiting time is {waiting_time}. Result: {lines[0] * waiting_time}")

if __name__ == "__main__":
    part_1()
