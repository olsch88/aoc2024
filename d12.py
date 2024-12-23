from collections import deque, defaultdict
import time


def read_data(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        raw_data = f.readlines()
    data = []
    for line in raw_data:
        data.append(list(line.strip()))
    return data


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


def add_rim(garden: list[list[str]]) -> list[list[str]]:
    garden.insert(0, ["*"] * len(garden[0]))
    garden.append(["*"] * len(garden[0]))
    for line in garden:
        line.insert(0, "*")
        line.append("*")
    return garden


def measure_region(
    garden: list[list[str]], start: tuple[int, int], letter: str, neighbors: dict
) -> tuple[int, int]:
    """traverses the region.
    returns (area, circumference)
    """
    queue = deque()
    visited = set()
    area = 0
    perimeter = 0
    queue.append(start)
    while len(queue) > 0:
        current_pos = queue.popleft()
        if current_pos in visited:
            continue
        area += 1
        visited.add(current_pos)
        for neighbor in neighbors[current_pos]:
            if neighbor in visited:
                continue
            if garden[neighbor[0]][neighbor[1]] == letter:

                queue.append(neighbor)
            else:
                perimeter += 1
    return (area, perimeter, visited)


def measure_edges(
    garden: list[list[str]], start: tuple[int, int], letter: str, neighbors: dict
) -> tuple[int, int]:
    """traverses the region.
    returns (area, circumference)
    """
    queue = deque()
    visited = set()
    area = 0
    perimeter = 0
    edges = 0
    corner_count = defaultdict(
        int
    )  # counts the number of tiles that are adjectend to a corner
    queue.append(start)
    while len(queue) > 0:
        current_pos = queue.popleft()
        if current_pos in visited:
            continue
        area += 1
        corner_count[(current_pos)] += 1
        corner_count[(current_pos[0] + 1, current_pos[1])] += 1
        corner_count[(current_pos[0] + 1, current_pos[1] + 1)] += 1
        corner_count[(current_pos[0], current_pos[1] + 1)] += 1
        visited.add(current_pos)
        for neighbor in neighbors[current_pos]:
            if neighbor in visited:
                continue
            if garden[neighbor[0]][neighbor[1]] == letter:

                queue.append(neighbor)
            else:
                perimeter += 1
    for corner_pos, count in corner_count.items():
        if count % 2 == 1:
            edges += 1
        if count == 2:
            if (
                garden[corner_pos[0]][corner_pos[1]] == letter
                and garden[corner_pos[0] - 1][corner_pos[1] - 1] == letter
            ):
                edges += 2
            if (
                garden[corner_pos[0] - 1][corner_pos[1]] == letter
                and garden[corner_pos[0]][corner_pos[1] - 1] == letter
            ):
                edges += 2
    return (area, perimeter, edges, visited)




def solve_part1(filename: str) -> int:
    garden = read_data(filename)
    garden = add_rim(garden)
    neighbors = get_neighbors((len(garden), len(garden[0])))
    visited = set()
    total_price = 0
    for row in range(1, len(garden) - 1):
        for col in range(1, len(garden[0]) - 1):
            if (row, col) in visited:
                continue

            current_letter = garden[row][col]
            region_area, region_perimeter, visited_region = measure_region(
                garden, (row, col), current_letter, neighbors
            )
            visited.update(visited_region)
            total_price += region_area * region_perimeter

    return total_price


def solve_part2(filename: str) -> int:
    garden = read_data(filename)
    garden = add_rim(garden)
    neighbors = get_neighbors((len(garden), len(garden[0])))
    visited = set()
    total_price = 0
    for row in range(1, len(garden) - 1):
        for col in range(1, len(garden[0]) - 1):
            if (row, col) in visited:
                continue

            current_letter = garden[row][col]
            region_area, region_perimeter, region_edges, visited_region = (
                measure_edges(garden, (row, col), current_letter, neighbors)
            )
            visited.update(visited_region)
            total_price += region_area * region_edges
    return total_price


if __name__ == "__main__":
    # print(read_data("d12_sample.txt"))

    start = time.perf_counter()
    print(solve_part1("d12_input.txt"))
    print(f"Runtime: {time.perf_counter()-start:.4f}")
    start = time.perf_counter()
    print(solve_part2("d12_input.txt"))
    print(f"Runtime: {time.perf_counter()-start:.4f}")
    # part2 : 900706 to low
