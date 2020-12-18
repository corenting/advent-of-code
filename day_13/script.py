from functools import reduce

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



# Chinese remainder theorem code from rosetta code
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def part_2():
    lines = [line for line in get_lines()[1].split(',')]
    depart_target = {}
    offset = 0
    for line in lines:
        if line != "x":
            depart_target[int(line)] = offset
        offset += 1
    line_ids = [line for line, _ in depart_target.items()]
    line_modulos = [-offset % line for line, offset in depart_target.items()]

    result = chinese_remainder(line_ids, line_modulos)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    part_2()
