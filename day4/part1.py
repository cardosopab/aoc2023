def sum_of_points(file_name):
    total = 0

    with open(file_name, "r") as file:
        text = file.read().splitlines()

    for line in text:
        # win_count = 0
        first, result = line.split("|")
        guess = first.split(":")[1]

        guess_nums = [int(x) for x in guess.split()]
        result_nums = [int(x) for x in result.split()]

        # Match intersecting numbers
        wins = len(set(guess_nums).intersection(set(result_nums)))

        # Using 2 to the power
        if wins > 0:
            total += 2 ** (wins - 1)

        # Using iteration
        # for i in range(wins):
        #     if win_count == 0:
        #         win_count = 1
        #     else:
        #         win_count *= 2
        # total += win_count

    return total


print(sum_of_points("day4/example.txt"))  # 13
print(sum_of_points("day4/puzzle.txt"))  # 1st 44681; final 22488
