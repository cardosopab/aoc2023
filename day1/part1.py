import re


def sum_of_calibration_values(file_name):
    with open(file_name, "r") as file:
        text = file.read().splitlines()
    total = 0
    for l in text:
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


# print(sum_of_calibration_values("day1/example.txt"))  # 142
print(sum_of_calibration_values("day1/puzzle.txt"))  # 55386
