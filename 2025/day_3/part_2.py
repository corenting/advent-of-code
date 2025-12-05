with open('input', 'r') as input_file:
    lines = [i.strip() for i in input_file.readlines()]

def calc(digits_required):
    total_output = 0

    num_length = len(lines[0])
    for current_line in lines:
        nums = [int(battery) for battery in current_line]
        my_digits = []
        prev_idx = 0
        for current_count in range(0, 12):

            end = num_length - digits_required + current_count + 1
            nums_slice = nums[prev_idx: end]
            max_value = max(nums_slice)
            max_index = nums_slice.index(max_value)
            my_digits.append(max_value)
            prev_idx = prev_idx + max_index + 1

        line_output = int("".join(str(i) for i in my_digits))
        total_output += line_output

    return total_output


print(f"Step 2: {calc(12)}")
