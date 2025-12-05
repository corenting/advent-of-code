with open('input', 'r') as input_file:
    lines = [i.strip() for i in input_file.readlines()]

total_output = 0
digits_required = 2

bank_length = len(lines[0])

for bank in lines:
    nums = [int(battery) for battery in bank]
    my_digits = []

    digits_to_ignore = digits_required - 1
    current_count = 0
    prev_idx = 0
    while current_count < digits_required:

        if current_count == 0:
            nums_slice = nums[:-1]
        else:
            nums_slice = nums[prev_idx + 1:]

        max_value = max(nums_slice)
        max_index = nums.index(max_value)
        my_digits.append(max_value)
        current_count += 1
        prev_idx = max_index


    total_output += int("".join(str(i) for i in my_digits))

print(f"Step 1: {total_output}")
