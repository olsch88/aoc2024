from pprint import pprint
from collections import deque
import time

NEIGHBORS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def read_bytes(file: str) -> list[tuple[int, int]]:
    with open(file, "r") as f:
        raw_data = f.readlines()
    byte_coordinates = []
    for line in raw_data:
        parts = line.strip().split(",")
        byte_coordinates.append((int(parts[0]), int(parts[1])))
    return byte_coordinates


def generate_map(coordinates: list[tuple[int, int]], dimension: int) -> list[list[str]]:
    maze = [["." for col in range(dimension)] for row in range(dimension)]
    for col, row in coordinates:
        maze[row][col] = "#"
    return maze


def find_path(maze: list[list[str]], start: tuple[int, int], end: tuple[int, int]):
    queue = deque()
    visited = set()
    start_length = 0
    shortest_path = 999_999
    queue.append((start, start_length))
    while len(queue) > 0:
        current_pos, current_len = queue.popleft()
        if current_pos in visited:
            continue
        if current_len > shortest_path:
            continue
        if current_pos == end:
            shortest_path = min(shortest_path, current_len)
            continue
        visited.add(current_pos)
        for neigbor in NEIGHBORS:
            next_row = current_pos[0] + neigbor[0]
            next_col = current_pos[1] + neigbor[1]
            if not 0 <= next_row < len(maze):
                continue
            if not 0 <= next_col < len(maze[0]):
                continue
            if maze[next_row][next_col] == ".":
                queue.append(((next_row, next_col), current_len + 1))
    return shortest_path


def solve_part1(data, dimension: int,limit: int) -> int:
    
    maze = generate_map(data[:limit], dimension + 1)
    path_length = find_path(maze, (0, 0), (dimension, dimension))
    return path_length


def solve_part2(data, dimension: int) -> tuple[int, int]:
    for limit in range(len(data)):
        maze = generate_map(data[:limit], dimension + 1)
        path_length = find_path(maze, (0, 0), (dimension, dimension))
        if path_length==999_999:
            return data[limit-1]
    

if __name__ == "__main__":
    sample_data = read_bytes("d18_sample.txt")
    print(solve_part1(sample_data, 6, 12))
    data = read_bytes("d18_input.txt")
    print(solve_part1(data, 70, 1024))
    
    sample_data = read_bytes("d18_sample.txt")
    print(solve_part2(sample_data, 6))
    
    start= time.perf_counter()
    data = read_bytes("d18_input.txt")
    print(solve_part2(data, 70))
    print(f"Runtime: {time.perf_counter()-start:.2f} s")
