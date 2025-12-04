from itertools import batched


with open('input', 'r') as input_file:
    line = next(input_file)

ranges = [i for i in line.split(",") if i != '\n']
total_step2 = 0
for current_range in ranges:
    start_number, end_number = current_range.split("-")
    start_number = int(start_number)
    end_number = int(end_number)

    for i in range(start_number, end_number + 1):

        num_as_str = str(i)
        len_num = len(num_as_str)

        current_size = 1
        sizes_to_check = [current for current in range(1, len_num ) if len_num % current == 0]
        for current_size in sizes_to_check:
            mini_batch = list(batched(num_as_str, current_size))
            #print(f"Num is {i}, {mini_batch = }, {current_size = }")

            if all(x == mini_batch[0] for x in mini_batch):
                total_step2 += i
                break


print(f"Step 2: {total_step2}")
