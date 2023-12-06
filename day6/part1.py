def sum_of_points(file_name):
    total = 1

    with open(file_name, "r") as file:
        text = file.read().splitlines()

    time, distance = text[0].split(":")[1].split(), text[1].split(":")[1].split()
    time, distance = [int(x) for x in time], [int(x) for x in distance]

    for t, d in zip(time, distance):
        boat_total = 0
        for i in range(1, t):
            # i will be the time held/speed
            if (t - i) * i > d:
                boat_total += 1
        total *= boat_total

    return total


print(sum_of_points("day6/example.txt"))  # 288
print(sum_of_points("day6/puzzle.txt"))  # 138915
