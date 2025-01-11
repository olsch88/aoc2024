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
                if (distances[current] - distances[(next_x, next_y)] )-2> 1:
                    save_counter[distances[current] - distances[(next_x, next_y)]-2] += 1
                    
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
    counter =0
    for key, value in shortcut_counter.items():
        # print(f"There are {value} cheats, that save {key} picoseconds")
        if key >= 100:
            counter += value
        
    # print(shortcut_counter)
    return counter


if __name__ == "__main__":
    start = time.time()
    maze = read_maze("d20_input.txt")
    print(solve_part1(maze))
    print("Execution time:", time.time() - start)
    # part 1_ 1310 too low