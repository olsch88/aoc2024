from collections import deque, defaultdict
import time

NEIGHBORS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
POSSIBLE_TELEPORTS_PART1 = [
    (0, 2),
    (0, -2),
    (2, 0),
    (-2, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]

POSSIBLE_TELEPORTS_PART2 = []
for row in range(-20, 21):
    for column in range(-20, 21):
        if abs(row) + abs(column) < 21 and abs(row) + abs(column) > 1:
            POSSIBLE_TELEPORTS_PART2.append((row, column))
            # POISSIBLE_TELEPORTS_PART2.append((-row, -column))
            # POISSIBLE_TELEPORTS_PART2.append((row, -column))
            # POISSIBLE_TELEPORTS_PART2.append((-row, column))
# print(POSSIBLE_TELEPORTS_PART2)


def read_maze(file: str) -> list[str]:
    with open(file, "r") as f:
        raw_data = f.readlines()
    return [line.strip() for line in raw_data]


def find_start(maze: list[str]) -> tuple[int, int]:
    for row_num, line in enumerate(maze):
        for col_num, tile in enumerate(line):
            if tile == "S":
                return (row_num, col_num)


def find_end(maze: list[str]) -> tuple[int, int]:
    for row_num, line in enumerate(maze):
        for col_num, tile in enumerate(line):
            if tile == "E":
                return (row_num, col_num)


def get_distances_to_start(maze: list[str]) -> dict[tuple[int, int], int]:
    start = find_end(maze)
    # print(start)
    distances = {start: 0}
    queue = deque()
    queue.append(start)
    while len(queue) > 0:
        current = queue.popleft()
        # print(current)

        for neighbor in NEIGHBORS:
            next_x, next_y = current[0] + neighbor[0], current[1] + neighbor[1]
            if maze[next_x][next_y] not in ".S":
                continue
            if (next_x, next_y) not in distances:
                distances[(next_x, next_y)] = distances[current] + 1
                queue.append((next_x, next_y))
    return distances


def find_shortcut(maze, distances):
    start = find_start(maze)
    end = find_end(maze)
    queue = deque()
    queue.append(start)
    visited = set()
    save_counter = defaultdict(int)
    while len(queue) > 0:
        current = queue.popleft()
        visited.add(current)
        for neighbor in POSSIBLE_TELEPORTS_PART1:
            next_x, next_y = current[0] + neighbor[0], current[1] + neighbor[1]
            if not (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0])):
                continue
            if maze[next_x][next_y] not in ".E":
                continue
            if (next_x, next_y) in distances:
                if (distances[current] - distances[(next_x, next_y)]) - 2 > 1:
                    save_counter[
                        distances[current] - distances[(next_x, next_y)] - 2
                    ] += 1

        for neighbor in NEIGHBORS:
            next_x, next_y = current[0] + neighbor[0], current[1] + neighbor[1]
            if maze[next_x][next_y] not in ".E":
                continue
            if (next_x, next_y) not in visited:
                queue.append((next_x, next_y))
    return save_counter


def find_shortcut_v2(maze, distances, range):
    start = find_start(maze)
    end = find_end(maze)
    queue = deque()
    queue.append(start)
    visited = set()
    save_counter = defaultdict(int)
    start_and_end = set()
    debug_counter = 0
    while len(queue) > 0:
        current = queue.popleft()
        visited.add(current)
        for target in POSSIBLE_TELEPORTS_PART2:
            next_x, next_y = current[0] + target[0], current[1] + target[1]
            distance = abs((abs(next_x) - abs(current[0]))) + abs(
                (abs(next_y) - abs(current[1]))
            )
            if not (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0])):
                continue
            if maze[next_x][next_y] not in ".E":
                continue
            if (current, (next_x, next_y)) in start_and_end:
                continue
            start_and_end.add((current, (next_x, next_y)))
            if (next_x, next_y) in distances:
                # if distances[current] - distances[(next_x, next_y)] - distance== 72:
                #     # print(abs(next_x) - abs(current[0]))#
                #     # print(abs(next_y) - abs(current[1]))#
                #     # print(distance)
                #     print(f"{current}-> {(next_x, next_y)} Distance without: {distances[current]} distance with: {distances[(next_x, next_y)]+distance}")
                #     debug_counter+=1
                if current == start and (next_x, next_y) == (7, 3):
                    print(distance)
                    print(
                        f"Teleporting to {(next_x, next_y)} saves {distances[current] - distances[(next_x, next_y)]-distance} picoseconds"
                    )
                if (distances[current] - distances[(next_x, next_y)]) - distance > 1:
                    save_counter[
                        distances[current] - distances[(next_x, next_y)] - distance
                    ] += 1

        for neighbor in NEIGHBORS:
            next_x, next_y = current[0] + neighbor[0], current[1] + neighbor[1]
            if maze[next_x][next_y] not in ".E":
                continue
            if (next_x, next_y) not in visited:
                queue.append((next_x, next_y))

    return save_counter


def solve_part1(maze: list[str]) -> int:
    distances = get_distances_to_start(maze)
    # print(distances)
    end = find_end(maze)
    shortcut_counter = find_shortcut(maze, distances)
    counter = 0
    for key, value in shortcut_counter.items():
        # print(f"There are {value} cheats, that save {key} picoseconds")
        if key >= 100:
            counter += value

    # print(shortcut_counter)
    return counter


def solve_part2(maze: list[str]) -> int:
    distances = get_distances_to_start(maze)
    # print(distances)
    end = find_end(maze)
    shortcut_counter = find_shortcut_v2(maze, distances, range=20)
    counter = 0
    for key, value in shortcut_counter.items():
        if key >= 100:
            counter += value
            # print(f"There are {value} cheats, that save {key} picoseconds")

    # print(shortcut_counter)
    return counter


if __name__ == "__main__":
    start = time.time()
    maze = read_maze("d20_input.txt")
    print(solve_part1(maze))
    print("Execution time:", time.time() - start)
    start = time.time()
    print(solve_part2(maze))
    print("Execution time:", time.time() - start)
    # part 2_  2209778 to high
