from collections import defaultdict


def sum_of_gear_ratios(file_name):
    match_dict = defaultdict(list)
    total = 0

    with open(file_name, "r") as file:
        text = file.read().splitlines()

    for y_index, y_value in enumerate(text):
        number = 0
        match = None
        y_value += "."

        for x_index, x_value in enumerate(y_value):
            if not x_value.isdigit():
                if match is not None:
                    match_dict[match].append(number)
                number = 0
                match = None

            else:
                number = number * 10 + int(x_value)
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ny, nx = y_index + dy, x_index + dx
                        if (
                            0 <= ny < len(text)
                            and 0 <= nx < len(text[y_index])
                            and text[ny][nx] == "*"
                        ):
                            match = (ny, nx)

    for m in match_dict.keys():
        if len(match_dict[m]) == 2:
            total += match_dict[m][0] * match_dict[m][1]

    return total


# print(sum_of_gear_ratios("day3/example.txt"))  # 467835
print(sum_of_gear_ratios("day3/puzzle.txt"))  # too low: 84226109; final 84399773
