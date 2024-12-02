def read_data(filename: str) -> list[list]:
    with open(filename, "r") as f:
        data = f.readlines()
    processed_data = []
    for line in data:
        processed_data.append([int(i) for i in line.strip().split()])
    return processed_data


def is_increasing(line: list[int]) -> bool:
    for i in range(1, len(line)):
        if line[i] <= line[i - 1]:
            return False
    return True


def is_safe(line: list[int]) -> bool:
    if not is_increasing(line) and not is_increasing(line[::-1]):
        return False
    for i in range(1, len(line)):
        if abs(line[i - 1] - line[i]) > 3:
            return False
        if abs(line[i - 1] - line[i]) < 1:
            return False
    return True


def is_safe_damped(line: list[int]) -> bool:
    for i, _ in enumerate(line):
        current_line = line.copy()
        current_line.pop(i)
        if is_safe(current_line):
            return True
    return False


def solve_part1(data: list[list]) -> int:
    safe_count = 0
    for line in data:
        safe_count += is_safe(line)
    return safe_count


def solve_part2(data: list[list]):
    safe_count = 0
    for line in data:
        safe_count += is_safe_damped(line)
    return safe_count


if __name__ == "__main__":
    data = read_data("d2_input.txt")
    print("Solution Part1:")
    print(solve_part1(data))
    print("Solution Part2:")
    print(solve_part2(data))

