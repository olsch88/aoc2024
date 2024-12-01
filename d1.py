def read_data(filename: str) -> tuple[list, list]:
    with open(filename, "r") as f:
        data = f.readlines()

    first_list = []
    second_list = []
    for line in data:
        first_list.append(int(line.strip().split()[0]))
        second_list.append(int(line.strip().split()[1]))
    return (first_list, second_list)


def solve_part1(first_list: list, second_list: list) -> int:
    total_distance = 0
    for num1, num2 in zip(sorted(first_list), sorted(second_list)):
        total_distance += abs(num2 - num1)
    return total_distance


def solve_part2(first_list: list, second_list: list) -> int:
    score = 0
    for number in first_list:
        score += number * second_list.count(number)
    return score


if __name__ == "__main__":
    first, second = read_data("d1_input.txt")

    print(solve_part1(first, second))
    print(solve_part2(first, second))
