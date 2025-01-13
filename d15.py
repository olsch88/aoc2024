from pprint import pprint
from copy import deepcopy

DIRECTIONS = {"<": (0, -1), ">": (0, 1), "v": (-1, 0), "^": (1, 0)}


def read_map(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        raw_data = f.readlines()

    data = []
    for line in raw_data:
        if line == "\n":
            break
        new_line = []
        for c in line.strip():
            new_line.append(c)
        data.append(new_line)
    return data


def read_instructions(filename: str) -> list[str]:
    with open(filename, "r") as f:
        raw_data = f.readlines()

    data = []
    for line in raw_data:
        if "#" in line:
            continue
        if line == "\n":
            continue
        for arrow in line.strip():
            data.append(arrow)
    return data


def can_move(grid: list[list[str]], pos: tuple[int, int], direction: str):
    step = DIRECTIONS[direction]

    if grid[pos[0] + step[0]][pos[1] + step[1]] == "#":
        return False
    if grid[pos[0] + step[0]][pos[1] + step[1]] == ".":
        return True

    return can_move(grid, grid[pos[0] + step[0]][pos[1] + step[1]], direction)


def move_step(grid: list[list[str]], pos: tuple[int, int], direction: str):
    step = DIRECTIONS[direction]
    new_grid = deepcopy(grid)
    if grid[pos[0] + step[0]][pos[1] + step[1]] == "#":
        return new_grid, pos
    if grid[pos[0] + step[0]][pos[1] + step[1]] == ".":
        return new_grid, (pos[0] + step[0], pos[1] + step[1])
    if grid[pos[0] + step[0]][pos[1] + step[1]] == "O":
        pass
        # return new_grid, (pos[0]+step[0],pos[1]+step[1])


if __name__ == "__main__":
    pprint(read_map("d15_sample.txt"))
    print(read_instructions("d15_sample.txt"))
