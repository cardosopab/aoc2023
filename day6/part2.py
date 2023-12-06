def sum_of_points(file_name):
    total = 0

    with open(file_name, "r") as file:
        text = file.read().splitlines()

    time = text[0].split(":")[1].replace(" ", "")
    distance = text[1].split(":")[1].replace(" ", "")
    time, distance = int(time), int(distance)

    minimum = float("inf")
    maximum = float("-inf")
    for i in range(1, time):
        # i will be the time held/speed
        if (time - i) * i > distance:
            minimum = min(minimum, i)
            maximum = max(maximum, i)
            total += 1

    return total


# print(sum_of_points("day6/example.txt"))  # 71503
print(sum_of_points("day6/puzzle.txt"))  # 138915
