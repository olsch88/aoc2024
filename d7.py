from collections import deque
import time


def read_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    return data


def find_combination(calibration: str) -> bool:
    target = int(calibration.split(":")[0])
    values = [int(num) for num in calibration.split(":")[1].strip().split()]
    queue = deque()
    start_value = values[0]
    residual_values = values[1:]
    queue.append((start_value, residual_values))
    while len(queue) > 0:
        curent_value, remaining_values = queue.popleft()
        if remaining_values == [] and curent_value == target:
            return target
        if remaining_values == [] and curent_value != target:
            continue
        for operator in "*+":
            next_value = int(
                eval(str(curent_value) + operator + str(remaining_values[0]))
            )
            if next_value > target:
                continue
            queue.appendleft((next_value, remaining_values[1:]))

    return 0


def find_combination_part2(calibration: str) -> bool:
    target = int(calibration.split(":")[0])
    values = [int(num) for num in calibration.split(":")[1].strip().split()]
    queue = deque()
    start_value = values[0]
    residual_values = values[1:]
    queue.append((start_value, residual_values))
    while len(queue) > 0:
        curent_value, remaining_values = queue.popleft()
        if remaining_values == [] and curent_value == target:
            return target
        if remaining_values == [] and curent_value != target:
            continue
        for operator in "*+|":
            if operator == "|":
                next_value = int(str(curent_value) + str(remaining_values[0]))
            else:
                next_value = int(
                    eval(str(curent_value) + operator + str(remaining_values[0]))
                )
            if next_value > target:
                continue
            queue.appendleft((next_value, remaining_values[1:]))

    return 0


def solve_part1(data: list[str]) -> int:
    total_calibration_result = 0
    for calibration in data:
        total_calibration_result += find_combination(calibration)
    return total_calibration_result


def solve_part2(data: list[str]) -> int:
    total_calibration_result = 0
    for calibration in data:
        total_calibration_result += find_combination_part2(calibration)
    return total_calibration_result


if __name__ == "__main__":
    data = read_data("d7_input.txt")
    start = time.perf_counter()
    print(solve_part1(data))
    print(f"Runtime: {time.perf_counter()-start:.4f}s")
    start = time.perf_counter()
    print(solve_part2(data))
    print(f"Runtime: {time.perf_counter()-start:.4f}s")
