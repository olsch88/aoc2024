import re


def read_data(filename: str) -> str:
    with open(filename, "r") as f:
        data = f.readlines()
    total_line = ""
    for line in data:
        total_line = total_line + line
    return total_line


def mul(num1: int, num2: int) -> int:
    return num1 * num2


def solve_part1(data) -> int:
    regex = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    total = 0
    for item in regex.finditer(data):
        total += eval(item.group())

    return total


def solve_part2(data) -> int:
    regex_mul = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    # regex_do=re.compile(r"do\(\)")
    # regex_dont=re.compile(r"don't\(\)")
    total = 0
    enabled = True
    for item in regex_mul.finditer(data):
        if item.group() == "do()":
            enabled = True
            continue
        if item.group() == "don't()":
            enabled = False
            continue
        if enabled:
            total += eval(item.group())

    return total


if __name__ == "__main__":
    print("Sample Part 1")
    data = read_data("d3_sample.txt")
    print(solve_part1(data))
    data = read_data("d3_sample2.txt")
    print("Sample Part 2")
    print(solve_part2(data))

    data = read_data("d3_input.txt")
    print("Solution Part1")
    print(solve_part1(data))
    print("Solution Part2")
    print(solve_part2(data))
