import itertools

def get_lines():
    lines = []
    with open('input', 'r') as input_file:
        for line in input_file:
            lines.append(line.strip())
    return lines

def check_is_sum_of_two(num_list, number):
    for x, y in itertools.combinations(num_list, 2):
        if number == x + y:
            return True
    return False

def part_1(preamble_length):

    numbers = [int(x) for x in get_lines()]

    for i in range(len(numbers) - preamble_length):
        previous = numbers[:i + preamble_length][-preamble_length:]
        num = numbers[i + preamble_length]
        if not check_is_sum_of_two(previous, num):
            print(f"Part 1: {num} is not sum of two previous")
            return num

def windowed_list(numbers, window_size):
    window_size -= 1
    for i in range(len(numbers)):
        ret = numbers[i + (i * window_size):][:window_size + 1]
        if not ret:
            return
        yield ret


def part_2(num_to_check):
    numbers = [int(x) for x in get_lines()]

    for j in range(len(numbers)):
        test_list = numbers[j:]
        for i in range(len(test_list)):
            lists = windowed_list(test_list, i)
            for item in lists:
                if len(item) > 1 and sum(item) == num_to_check:
                    print(f"Part 2: {min(item) + max(item)}")
                    return min(item) + max(item)


if __name__ == "__main__":
    ret = part_1(25)
    part_2(ret)
