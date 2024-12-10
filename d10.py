from collections import deque


def read_data(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        data = f.readlines()
    topo_map = []
    for line in data:
        this_line = []
        for number in line.strip():
            this_line.append(int(number))
        topo_map.append(this_line)
    return topo_map


def get_neighbors(map_size: tuple[int, int]) -> dict:
    neighbors = dict()
    for row in range(map_size[0]):
        for col in range(map_size[1]):
            neighbors[(row, col)] = []
            if row > 0:
                neighbors[((row, col))].append((row - 1, col))
            if col > 0:
                neighbors[((row, col))].append((row, col - 1))
            if row < (map_size[0] - 1):
                neighbors[((row, col))].append((row + 1, col))
            if col < (map_size[1] - 1):
                neighbors[((row, col))].append((row, col + 1))
    return neighbors


def find_starts(topo_map: list[list[int]]) -> list[tuple[int, int]]:
    starts = []
    for row_num, line in enumerate(topo_map):
        for col_num, num in enumerate(line):
            if num == 0:
                starts.append((row_num, col_num))
    return starts


def count_paths(topo_map: list[list[int]], start: tuple[int, int]) -> int:
    neighbors = get_neighbors((len(topo_map), len(topo_map[0])))
    path_count = 0
    start_num = 0
    nine_pos = set()
    queue = deque()
    queue.append((start, start_num))
    while len(queue) > 0:
        current_pos, current_num = queue.popleft()
        if current_num == 9:
            nine_pos.add((current_pos))
            path_count += 1
            continue
        for neighbor in neighbors[current_pos]:
            if topo_map[neighbor[0]][neighbor[1]] == current_num + 1:
                queue.append((neighbor, current_num + 1))

    return (len(nine_pos), path_count)


def solve_part1(topo_map, starts) -> int:
    total_score = 0
    for start in starts:
        total_score += count_paths(topo_map, start)[0]
    return total_score


def solve_part2(topo_map, starts) -> int:
    total_score = 0
    for start in starts:
        total_score += count_paths(topo_map, start)[1]
    return total_score


if __name__ == "__main__":
    topo_map = read_data("d10_input.txt")
    starts = find_starts(topo_map)
    print(solve_part1(topo_map, starts))
    print(solve_part2(topo_map, starts))
