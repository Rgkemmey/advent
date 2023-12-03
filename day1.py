file = open("day_1_input.txt")

def str_to_int(line):
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    return line

def extract_calibration_values(file):
    total = 0

    for line in file:
        new_line = str_to_int(line)
        nums = [char for char in new_line if char.isdigit()]
        if len(nums) == 1:
            nums.append(nums[0])
        n = nums[0] + nums[len(nums) - 1]
        total = total + int(n)

    return total

result = extract_calibration_values(file)

print(result)
