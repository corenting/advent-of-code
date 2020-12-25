from collections import defaultdict

def get_start_list():
    with open('input', 'r') as input_file:
        for line in input_file:
            return [int(num) for num in line.split(',')]

def update_turn_history(turn_history, turn, num):
    if num in turn_history:
        turn_history[num].append(turn)
    else:
        turn_history[num] = [turn]
    return turn_history

def main(stop_at):
    ints = get_start_list()

    turn = 0
    nums_count = {}
    nums_last_turns = {}
    last_spoken = None

    for num in ints:
        nums_count[num] = nums_count.get(num, 0) + 1
        turn += 1
        nums_last_turns = update_turn_history(nums_last_turns, turn, num)
        last_spoken = num

    while True:
        if turn == stop_at:
            exit(0)

        if nums_count.get(last_spoken, 0) == 1:
            last_spoken = 0
        else:
            last_spoken = nums_last_turns[last_spoken][-1] - nums_last_turns[last_spoken][-2]

        turn += 1
        nums_count[last_spoken] = nums_count.get(last_spoken, 0) + 1

        nums_last_turns = update_turn_history(nums_last_turns, turn, last_spoken)

        if turn == stop_at:
            print(f"Turn {turn} - Say: {last_spoken}")


if __name__ == "__main__":
    main(30000000)
