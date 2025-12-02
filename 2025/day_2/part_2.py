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

        current_size = 1
        while current_size < len(num_as_str):
            mini_batch = [i for i in batched(num_as_str, current_size)]
            len_batch = len(mini_batch)
            if all(x == mini_batch[0] for x in mini_batch):
                total_step2 += i
                break
            current_size += 1


print(f"Step 2: {total_step2}")
