from pprint import pprint
from dataclasses import dataclass
from collections import deque, defaultdict

from heapq import heapify, heappop, heappush

NEIGHBORS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# @dataclass(order=True)
# class Node:
#     priority: int
#     item: Any=field(compare=False)


@dataclass(frozen=True, eq=True)
class Node:
    kind: str
    pos: tuple[int, int]
    direction: tuple[int, int]


def read_maze(file: str) -> list[list[str]]:
    with open(file, "r") as f:
        raw_data = f.readlines()
    data = [list(line.strip()) for line in raw_data]

    return data


def traverse_maze(
    maze: list[list[str]],
    start_pos: tuple[int, int],
    start_dir: tuple[int, int],
    target_pos: tuple[int, int],
):
    queue = deque()
    min_cost = 999999
    cost = 0
    queue.append((start_pos, start_dir, cost))
    priority_queue = []
    # priority_queue = heapify(priority_queue)
    heappush(priority_queue, (0, start_pos, start_dir, cost))
    visited = []
    # while len(priority_queue) > 0:
    while len(queue) > 0:
        # print(len(priority_queue), len(visited))
        # print(len(queue), len(visited))
        current_pos, current_dir, current_cost = queue.popleft()
        # priority, current_pos, current_dir, current_cost = heappop(priority_queue)
        current_distance = abs(current_pos[0] - target_pos[0]) + abs(
            current_pos[1] - target_pos[1]
        )

        if current_pos == target_pos:
            print(current_cost)
            print(current_dir)
            min_cost = min(min_cost, current_cost)
            continue
        else:
            visited.append((current_pos, current_dir))
            if current_cost > min_cost:
                continue
            # visited[current_pos] += 1

        for direction in DIRECTIONS:
            if direction == current_dir:
                added_cost = 1
            elif (current_pos[0] + direction[0]) == 0 and (
                current_pos[1] + direction[1]
            ) == 0:  # 180° turn
                continue
                # added_cost = 2001
            else:
                added_cost = 1001
            # if (
            #     current_pos[0] + direction[0],
            #     current_pos[1] + direction[1],
            # ) == target_pos:
            #     min_cost = min(min_cost, current_cost + added_cost)
            if (
                maze[current_pos[0] + direction[0]][current_pos[1] + direction[1]]
                not in "#S"
                and (
                    (current_pos[0] + direction[0], current_pos[1] + direction[1]),
                    direction,
                )
                not in visited
            ):
                queue.append(
                    (
                        (current_pos[0] + direction[0], current_pos[1] + direction[1]),
                        direction,
                        current_cost + added_cost,
                    )
                )
                # heappush(
                #     priority_queue,
                #     (
                #         current_distance,
                #         (current_pos[0] + direction[0], current_pos[1] + direction[1]),
                #         direction,
                #         current_cost + added_cost,
                #     ),
                # )
    return min_cost


def get_pos(maze: list[list[str]], target: str):
    for row_num, row in enumerate(maze):
        for col_num, letter in enumerate(row):
            if letter == target:
                return (row_num, col_num)


def solve_part1(maze: list[list[str]]) -> int:
    start = get_pos(maze, "S")
    print(start)
    end = get_pos(maze, "E")
    print(end)
    return traverse_maze(maze, start, (0, 1), end)


if __name__ == "__main__":
    mazee = read_maze("d16_input.txt")
    print(solve_part1(mazee))
    # part1: to high 89404
