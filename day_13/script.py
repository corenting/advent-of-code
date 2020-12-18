def get_lines():
    lines = []
    with open('input', 'r') as input_file:
        for line in input_file:
            lines.append(line.strip())
    return lines

def check_depart_at_time(line, time):
    return time % line == 0

def part_1():
    lines = get_lines()
    start_time = int(lines[0])
    bus_list = [int(line) for line in lines[1].split(',') if line != "x"]
    max_time = start_time + 100

    schedule = {}
    for i in range(start_time, max_time):
        lines_at_time = [line for line in bus_list if check_depart_at_time(line, i)]
        if len(lines_at_time) > 0:
            schedule[i] = lines_at_time

    # Get earliest one
    time, lines = list(schedule.items())[0]
    waiting_time = time - start_time
    print(f"Part 1: Line {lines[0]}, waiting time is {waiting_time}. Result: {lines[0] * waiting_time}")


def part_2():
    lines = get_lines()
    start_time = 200000000000000

    max_time = 300000000000000

    lines = [line for line in lines[1].split(',')]
    depart_target = {}
    offset = 0
    for line in lines:
        if line != "x":
            depart_target[int(line)] = offset
        offset += 1

    # Find depart time for first line
    first_line, _ = list(depart_target.items())[0]
    first_line_departures = (i for i in range(start_time, max_time) if check_depart_at_time(first_line, i))

    for departure in first_line_departures:
        ok = True
        for line in list(depart_target.keys())[1:]:
            if not check_depart_at_time(line, departure + depart_target[line]):
                ok = False
                break

        if ok:
            print(f"Part 2: {departure}")
            return


    import pdb; pdb.set_trace()
    pass

if __name__ == "__main__":
    part_2()
