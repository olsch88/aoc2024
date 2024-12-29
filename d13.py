import time


def read_data(file: str) -> list[dict[str, tuple[int, int]]]:
    with open(file, "r") as f:
        raw_data = f.readlines()
    claws = []
    this_claw = dict()
    for line in raw_data:
        if "A" in line:
            parts = line.split(":")
            x = int(parts[1].split(",")[0].split("X")[1])
            y = int(parts[1].split(",")[1].split("Y")[1])
            this_claw["A"] = (x, y)
        if "B" in line:
            parts = line.split(":")
            x = int(parts[1].split(",")[0].split("X")[1])
            y = int(parts[1].split(",")[1].split("Y")[1])
            this_claw["B"] = (x, y)
        if "Prize" in line:
            parts = line.split(":")
            x = int(parts[1].split(",")[0].split("=")[1])
            y = int(parts[1].split(",")[1].split("=")[1])
            this_claw["Prize"] = (x, y)
        if line == "\n":
            claws.append(this_claw)
            this_claw = dict()
    claws.append(this_claw)
    return claws


def calc_determinante(x1: int, y1: int, x2: int, y2: int) -> int:
    return x1 * y2 - x2 * y1


def calc_tokens(claw: dict[str, tuple[int, int]]) -> int:
    A = calc_determinante(
        claw["Prize"][0], claw["Prize"][1], claw["B"][0], claw["B"][1]
    ) / calc_determinante(claw["A"][0], claw["A"][1], claw["B"][0], claw["B"][1])
    # print(A)
    B = calc_determinante(
        claw["A"][0], claw["A"][1], claw["Prize"][0], claw["Prize"][1]
    ) / calc_determinante(claw["A"][0], claw["A"][1], claw["B"][0], claw["B"][1])
    # print(B)
    if not int(A) == A or not int(B) == B:
        return 0
    return int(A * 3 + B)


def solve_part1(claw_data: list[dict[str, tuple[int, int]]]) -> int:
    total_tokens = 0
    for claw in claw_data:
        total_tokens += calc_tokens(claw)
    return total_tokens


def solve_part2(claw_data: list[dict[str, tuple[int, int]]]) -> int:
    offset = 10000000000000
    total_tokens = 0
    for claw in claw_data:
        claw["Prize"] = (claw["Prize"][0] + offset, claw["Prize"][1] + offset)
    for claw in claw_data:
        total_tokens += calc_tokens(claw)
    return total_tokens


if __name__ == "__main__":
    start = time.perf_counter()
    data = read_data("d13_input.txt")
    print(solve_part1(data))
    print(f"{time.perf_counter()-start:.4f}")
    start = time.perf_counter()
    data = read_data("d13_input.txt")
    print(solve_part2(data))
    print(f"{time.perf_counter()-start:.4f}")
