import re
from collections import defaultdict


def sum_of_power_of_sets(file_name):
    total = 0
    color_list = ["red", "green", "blue"]

    with open(file_name, "r") as file:
        text = file.read().splitlines()

    for line_index, line in enumerate(text):
        colon_index = line.index(":")
        trimmed = line[colon_index + 1 : :]
        trimmed.replace(";", ",")
        sets = trimmed.split(",")
        min_cubes = defaultdict(lambda: float("-inf"))
        set_power = 1

        for set_index, s in enumerate(sets):
            num_place = re.findall("\d+", s)
            color_place = re.findall("[a-zA-Z]+", s)

            for num_index in range(len(num_place)):
                min_cubes[color_place[num_index]] = max(
                    min_cubes[color_place[num_index]], int(num_place[num_index])
                )

        for value in min_cubes.values():
            set_power *= value
        total += set_power

    return total


# print(sum_of_power_of_sets("day2/example.txt"))  # 2286
print(sum_of_power_of_sets("day2/puzzle.txt"))  # 70387
