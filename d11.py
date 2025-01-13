from collections import defaultdict
import time


def read_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        raw_data = f.readline()
    data_list = [int(num) for num in raw_data.strip().split()]

    data_dict = defaultdict(int)
    for num in data_list:
        data_dict[num] += 1

    return data_dict


def blink_once(stone_dict: dict[int, int]) -> dict[int, int]:
    next_blink = stone_dict.copy()
    for stone_number, stone_count in stone_dict.items():
        if stone_number == 0:
            next_blink[1] += stone_count
            next_blink[0] -= stone_count
        elif len(str(stone_number)) % 2 == 0:
            half = int(len(str(stone_number)) / 2)
            next_blink[int(str(stone_number)[:half])] += stone_count
            next_blink[int(str(stone_number)[half:])] += stone_count
            next_blink[stone_number] -= stone_count
        else:
            next_blink[stone_number * 2024] += stone_count
            next_blink[stone_number] -= stone_count
    return next_blink


def count_stones(stones: dict[int, int]) -> int:
    return sum(stones.values())


def solve_part1(filename: str) -> int:
    stones = read_data(filename)

    for _ in range(25):
        stones = blink_once(stones)
    return count_stones(stones)


def solve_part2(filename: str) -> int:
    stones = read_data(filename)

    for _ in range(75):
        stones = blink_once(stones)
    return count_stones(stones)


if __name__ == "__main__":
    start = time.perf_counter()
    print(solve_part1("d11_input.txt"))
    print(f"Runtime: {time.perf_counter()-start}")
    start = time.perf_counter()
    print(solve_part2("d11_input.txt"))
    print(f"Runtime: {time.perf_counter()-start}")
