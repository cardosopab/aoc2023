from collections import defaultdict


def sum_of_points(file_name):
    win_count = defaultdict(int)

    with open(file_name, "r") as file:
        text = file.read().splitlines()

    for i, line in enumerate(text):
        win_count[i] += 1
        front, result = line.split("|")
        guess = front.split(":")[1]

        guess_nums = [int(x) for x in guess.split()]
        result_nums = [int(x) for x in result.split()]

        # Match intersecting numbers
        wins = len(set(guess_nums).intersection(result_nums))

        # Iterating through copies
        for j in range(wins):
            # Aggregating each copy's win count for the current card
            win_count[i + j + 1] += win_count[i]

    return sum(win_count.values())


print(sum_of_points("day4/example.txt"))  # 30
# print(sum_of_points("day4/puzzle.txt"))  # 7013204
