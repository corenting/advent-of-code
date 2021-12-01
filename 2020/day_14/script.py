import re
import itertools

def get_lines():
    lines = []
    with open('input', 'r') as input_file:
        for line in input_file:
            lines.append(line.strip())
    return lines

def get_mask(line, ignore_x=True):
    mask_string = line.split("=")[1].strip()
    mask = {}
    for i in range(len(mask_string)):
        chr = mask_string[i]
        if chr != "X" or not ignore_x:
            mask[i] = chr
    return mask

def get_line_info(line):
    pattern = 'mem\[(\d+)\] = (\d+)'
    regex_ret = re.search(pattern, line)

    return regex_ret.group(1), regex_ret.group(2)

def compute_masked_value(value, mask):
    computed_value = list(f"{int(value):036b}")
    for key, item in mask.items():
        computed_value[key] = item

    return int("".join(computed_value), 2)

def get_mem_sum(mem):
    sum = 0
    for mem_value in mem.values():
        sum += mem_value
    return sum

def part_1():
    lines = get_lines()
    mem = {}
    mask = get_mask(lines[0])

    for line in lines[1:]:
        if "mask" in line:
            mask = get_mask(line)
            continue
        mem_pos, value = get_line_info(line)
        mem[mem_pos] = compute_masked_value(value, mask)

    print(f"Part 1: {get_mem_sum(mem)}")

def get_address(mem_pos, mask):
    mask_bin = list(mask.values())
    computed_adr = list(f"{int(mem_pos):036b}")
    for i in range(36):
        mask_bin_chr = mask_bin[i]
        computed_adr_char = computed_adr[i]

        if mask_bin_chr == "0":
            value = computed_adr_char
        elif mask_bin_chr == "1":
            value = "1"
        else:
            value = "X"
        computed_adr[i] = value

    return computed_adr

def get_all_addresses(address):
    all_addresses = []
    possibilities = list(itertools.product(["0", "1"], repeat= address.count("X")))

    for possibility_num in range(len(possibilities)):
        x_pos = 0
        computed_addr = []
        for i in range(36):
            new_char = address[i]
            if address[i] == "X":
                new_char = possibilities[possibility_num][x_pos]
                x_pos += 1
            computed_addr.append(new_char)
        all_addresses.append(computed_addr)

    return all_addresses


def part_2():
    lines = get_lines()
    mem = {}
    mask = get_mask(lines[0], ignore_x=False)

    for line in lines[1:]:
        if "mask" in line:
            mask = get_mask(line, ignore_x=False)
            continue

        mem_pos, value = get_line_info(line)
        adr = get_address(mem_pos, mask)

        computed_addresses = get_all_addresses(adr)

        for addr in computed_addresses:
            int_addr = int("".join(addr), 2)
            mem[int_addr] = int(value)

    print(f"Part 2: {get_mem_sum(mem)}")

if __name__ == "__main__":
    part_1()
    part_2()
