import functools

map = []
with open('input', 'r') as input_file:
    for line in input_file:
        map.append(line.strip())
map = map[1:]  # remove first line (starting line)

conf = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

results = []
for x_slope, y_slope in conf:
    x = x_slope
    y = y_slope - 1
    trees = 0
    while y < len(map):
        line = map[y]
        if x >= len(line):
            x = x % len(line)

        if line[x] == "#":
            trees += 1

        x += x_slope
        y += y_slope

    print(f"Trees (right {x_slope}, down {y_slope}): {trees}")
    results.append(trees)

print(f"Total: {functools.reduce(lambda i,j : i*j, results)}")
