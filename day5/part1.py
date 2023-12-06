def min_location_number(file_name):
    total = float("inf")

    with open(file_name, "r") as file:
        text = file.read().splitlines()

    sections = []
    part = []
    text_len = len(text)
    for line_index, line in enumerate(text):
        if line != "":
            part.append(line)
        if line == "" or line_index == text_len - 1:
            sections.append(part)
            part = []
    seeds = sections[0][0].split(":")[1].split()
    for seed in seeds:
        output = int(seed)
        for section_index in range(1, len(sections)):
            # for section_index in range(1, 2):
            for map_index in range(1, len(sections[section_index])):
                values = sections[section_index][map_index].split()
                dest, src, ran = map(int, values)
                # print(sections[section_index][map_index])
                if src <= output < src + ran:
                    output = dest + output - src
                    break
            print(sections[section_index][0], output)
        total = min(total, output)

    return total


print(min_location_number("day5/example.txt"))  # 35
# print(min_location_number("day5/puzzle.txt"))  # 484023871
