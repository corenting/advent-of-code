with open('input', 'r') as input_file:
    line = next(input_file)

ranges = [i for i in line.split(",") if i != '\n']
total_step1 = 0
for current_range in ranges:
    start_number, end_number = current_range.split("-")
    start_number = int(start_number)
    end_number = int(end_number)

    for i in range(start_number, end_number + 1):

        num_as_str = str(i)
        digits_count = len(num_as_str)

        first_part = num_as_str[:digits_count // 2]
        second_part = num_as_str[digits_count // 2:]

        if (digits_count - 1) % 2 == 0:
            continue

        #print(f"{num_as_str = } {digits_count = } {first_part = } {second_part = }")

        if first_part == second_part:
            total_step1 += i

print(f"Step 1: {total_step1}")
