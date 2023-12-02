import re


def sum_of_possible_games(file_name):
    total = 0
    color_list = ["red", "green", "blue"]
    color_limits = [12, 13, 14]

    with open(file_name, "r") as file:
        text = file.read().splitlines()

    for line_index, line in enumerate(text):
        colon_index = line.index(":")
        trimmed = line[colon_index + 1 : :]
        sets = trimmed.split(";")
        check = [True] * len(sets)

        for set_index, s in enumerate(sets):
            num_place = re.findall("\d+", s)
            color_place = re.findall("[a-zA-Z]+", s)

            for j in range(len(color_place)):
                color_index = color_list.index(color_place[j])

                if int(num_place[j]) > color_limits[color_index]:
                    check[set_index] = False

        if False not in check:
            total += line_index + 1

    return total


# print(sum_of_possible_games("day2/example.txt"))  # 8
print(sum_of_possible_games("day2/puzzle.txt"))  # 1734
