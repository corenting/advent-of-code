def get_input() -> list[str]:
    lines = []
    with open('input', 'r') as input_file:
        for line in input_file:
            lines.append(line.strip())
    return lines

def split_input_by_block(lines) -> list[list[str]]:
    result = []
    working_item = []
    for item in lines:
        if not item:
            result.append(working_item)
            working_item = []
        else:
            working_item.append(item)
    result.append(working_item)
    return result

def parse_mapping(block: list[str], wanted_source_ids: list[int]) -> tuple[dict[int, int], str]:
    """
    Parse mapping but only for the wanted source ids.
    """
    mapping_header = block[0].replace(" map:", "").split("-to-")
    from_type = mapping_header[0]
    to_type = mapping_header[1]

    ret: dict[int, int] = {}
    for line in block[1:]:
        numbers = [int(i) for i in line.split(" ")]
        destination_range_start = numbers[0]
        source_range_start = numbers[1]
        range_length = numbers[2]

        # Check if any number is in the range
        range_has_a_wanted_src = False
        range_wanted_srcs: list[int] = []
        for src in wanted_source_ids:
            if source_range_start <= src <= source_range_start + range_length:
                range_has_a_wanted_src = True
                range_wanted_srcs.append(src)

        if not range_has_a_wanted_src:
            continue

        for src in range_wanted_srcs:
            ret[src] = destination_range_start + (src - source_range_start)

    # Add wanted seeds that are missing
    for src in wanted_source_ids:
        if src in ret:
            continue
        ret[src] = src

    return ret, f"{from_type}_{to_type}"

def get_seeds_location(seeds_to_be_planted: list[int], mappings: dict[str, dict[int, int]]) -> dict[int, int]:
    ret = {}
    for seed in seeds_to_be_planted:
        soil = mappings["seed_soil"][seed]
        fertilizer = mappings["soil_fertilizer"][soil]
        water = mappings["fertilizer_water"][fertilizer]
        light = mappings["water_light"][water]
        temperature = mappings["light_temperature"][light]
        humidity = mappings["temperature_humidity"][temperature]
        location = mappings["humidity_location"][humidity]
        ret[seed] = location

    return ret

lines = get_input()
blocks = split_input_by_block(lines)

# Get seeds to be planted
seeds_to_be_planted: list[int] = []
for seed_number in [int(i) for i in blocks[0][0].replace("seeds: ", "").split(" ")]:
    seeds_to_be_planted.append(seed_number)

# Get all the others mappings but only for the values wanted
# based on the previous mapping
mappings: dict[str, dict[int, int]] = {}
wanted_ids = seeds_to_be_planted
for block in blocks[1:]:
    block_mapping, mapping_name = parse_mapping(block, wanted_ids)
    mappings[mapping_name] = block_mapping
    wanted_ids = list(mappings[mapping_name].values())

# Get all seeds locations
seeds_locations = get_seeds_location(seeds_to_be_planted, mappings)

print(f"Part 1: {min(seeds_locations.values())}")
