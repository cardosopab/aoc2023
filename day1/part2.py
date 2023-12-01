import re


def sum_of_calibration_values(file_name):
    with open(file_name, "r") as file:
        text = file.read().splitlines()
    total = 0
    for l in text:
        l = l.replace("one", "o1e")
        l = l.replace("two", "t2o")
        l = l.replace("three", "t3e")
        l = l.replace("four", "f4r")
        l = l.replace("five", "f5e")
        l = l.replace("six", "s6x")
        l = l.replace("seven", "s7n")
        l = l.replace("eight", "e8t")
        l = l.replace("nine", "n9e")
        nums = re.findall("\d+", l)
        if len(nums[0]) > 1:
            a = nums[0][0]
        else:
            a = nums[0]

        if len(nums[-1]) > 1:
            b = nums[-1][-1]
        else:
            b = nums[-1]
        total += int(a + b)
    return total


# print(sum_of_calibration_values("day1/example2.txt"))  # 281
print(sum_of_calibration_values("day1/puzzle.txt"))  # 54824
