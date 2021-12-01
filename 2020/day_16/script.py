import re

def get_lines():
    lines = []
    with open('input', 'r') as input_file:
        for line in input_file:
            lines.append(line.strip())
    return lines

def split_array_on_empty(arr):
    ret = []
    curr = []
    for line in arr:
        if line:
            curr.append(line)
        else:
            ret.append(curr)
            curr = []

    ret.append(curr)
    return ret

def get_rules(arr):
    rules = []
    for elt in arr:
        regex_ret = re.search("([a-z]+): (\d+)-(\d+) or (\d+)-(\d+)", elt)
        rule = {
            'name': regex_ret.group(1),
            'limits': [
                (int(regex_ret.group(2)), int(regex_ret.group(3))),
                (int(regex_ret.group(4)), int(regex_ret.group(5)))
            ]
        }
        rules.append(rule)

    return rules

def get_ticket_from_str(str):
    return [int(elt) for elt in str.split(',')]

def get_nearby_tickets(arr):
    return [get_ticket_from_str(elt) for elt in arr]

def get_error_value_for_ticket(ticket, rules):
    error = 0
    for value in ticket:
        matched_rules = 0
        for rule in rules:
            for limit in rule['limits']:
                min_v, max_v = limit
                if min_v <= value <= max_v:
                    matched_rules += 1

        if matched_rules == 0:
            error += value

    return error

def day_1():
    lines = get_lines()
    elements = split_array_on_empty(lines)

    rules = get_rules(elements[0])
    my_ticket = get_ticket_from_str(elements[1][1:][0])
    nearby_tickets = get_nearby_tickets(elements[2][1:])

    error_rate = 0
    for ticket in nearby_tickets:
        error_rate += get_error_value_for_ticket(ticket, rules)

    print(error_rate)

if __name__ == "__main__":
    day_1()
