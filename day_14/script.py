import re

def get_lines():
    lines = []
    with open('input', 'r') as input_file:
        for line in input_file:
            lines.append(line.strip())
    return lines

def get_mask(line):
    mask_string = line.split("=")[1].strip()
    mask = {}
    for i in range(len(mask_string)):
        chr = mask_string[i]
        if chr != "X":
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

    return "".join(computed_value)

def get_mem_sum(mem):
    sum = 0
    for mem_value in mem.values():
        sum += int(mem_value, 2)
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

if __name__ == "__main__":
    part_1()
