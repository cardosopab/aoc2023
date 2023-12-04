def sum_of_part_numbers(file_name):
    total = 0

    with open(file_name, "r") as file:
        text = file.read().splitlines()

    for y_index, y_value in enumerate(text):
        number = 0
        match = False

        for x_index, x_value in enumerate(y_value):
            if not x_value.isdigit():
                if match:
                    total += number
                    match = False
                number = 0

            else:
                number = number * 10 + int(x_value)
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        ny, nx = y_index + dy, x_index + dx
                        if (
                            0 <= ny < len(text)
                            and 0 <= nx < len(text[y_index])
                            and text[ny][nx] != "."
                            and not text[ny][nx].isnumeric()
                        ):
                            match = True

    return total


print(sum_of_part_numbers("day3/example.txt"))  # 4361
print(sum_of_part_numbers("day3/puzzle.txt"))
# too low: 332700; too low: 436710; final 524899
