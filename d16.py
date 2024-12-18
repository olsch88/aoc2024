from pprint import pprint
from dataclasses import dataclass
from collections import deque

NEIGHBORS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


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


def find_nodes(maze: list[list[str]]) -> list[Node]:
    nodes = []
    for row_num, line in enumerate(maze):
        for col_num, tile in enumerate(line):
            if tile == "#":
                continue
            if tile == "S":
                nodes.append(Node("S", (row_num, col_num), (0, 1)))
            if tile == "E":
                for direction in DIRECTIONS:
                    nodes.append(Node("E", (row_num, col_num), direction))
            neighbor_count = 0
            for neigh in NEIGHBORS:
                if maze[row_num + neigh[0]][col_num + neigh[1]] == ".":
                    neighbor_count += 1
            if neighbor_count > 2:
                for direction in DIRECTIONS:
                    nodes.append(Node(".", (row_num, col_num), direction))

    return nodes


def find_next_nodes(
    maze: list[list[str]], nodes: list[tuple[tuple, tuple]]
) -> list[dict[tuple, dict]]:
    connections = dict()
    nodes_queue = deque()

    for node in nodes:
        start = node[0]
        start_direction = node[1]
        queue = deque()
        cost = 0
        queue.append((start, start_direction, cost))
        while len(queue > 0):
            current_pos, current_direction, current_cost = queue.popleft()


def find_next_nodes2(
    maze: list[list[str]], start=((13, 1), (0, 1))
) -> list[dict[Node, dict]]:
    connections = dict()
    nodes_found = []
    nodes_queue = deque()
    nodes_queue.append(start)
    while len(nodes_queue) > 0:
        this_node: tuple[tuple, tuple]
        this_connections = dict()
        this_node = nodes_queue.popleft()
        print(f"checking node: {this_node}")
        start = this_node[0]
        start_direction = this_node[1]
        queue = deque()
        cost = 0
        visited = []
        node_connections_found = []
        queue.append(
            (
                (start[0] + start_direction[0], start[1] + start_direction[1]),
                start_direction,
                cost + 1,
            )
        )
        for direction in DIRECTIONS:
            if direction == start_direction:
                continue
            if (start_direction[0] + direction[0]) == 0 and (
                start_direction[1] + direction[1]
            ) == 0:  # 180° turn
                queue.append(
                    (
                        (
                            start[0] + direction[0],
                            start[1] + direction[1],
                        ),
                        direction,
                        cost + 1000 + 1,
                    )
                )
                continue
            queue.append(
                (
                    (
                        start[0] + direction[0],
                        start[1] + direction[1],
                    ),
                    direction,
                    cost + 2000 + 1,
                )
            )
        while len(queue) > 0:
            current_pos, current_direction, current_cost = queue.popleft()
            if maze[current_pos[0]][current_pos[1]] == "#":
                continue
            if current_pos in visited:
                continue
            visited.append(current_pos)
            neighbor_count = 0
            for neigh in NEIGHBORS:
                if maze[current_pos[0] + neigh[0]][current_pos[1] + neigh[1]] == ".":
                    print(maze[10][1])
                    print(
                        f"Neigbour at: {(current_pos[0] + neigh[0], current_pos[1] + neigh[1])}"
                    )
                    neighbor_count += 1
            print(current_pos)
            print(neighbor_count)
            if neighbor_count > 2:  # we found a crossroad!
                if (current_pos, current_direction) not in node_connections_found:
                    this_connections[(current_pos, current_direction)] = current_cost
                    for direction in DIRECTIONS:
                        if (current_pos, direction) not in nodes_found:
                            nodes_queue.append((current_pos, direction))
                            nodes_found.append((current_pos, direction))
                            node_connections_found.append((current_pos, direction))
                    continue
                else:
                    print(f"{current_pos} already in nodes")
            if (
                maze[current_pos[0] + current_direction[0]][
                    current_pos[1] + current_direction[1]
                ]
                == "."
            ):
                queue.append(
                    (
                        (
                            current_pos[0] + current_direction[0],
                            current_pos[1] + current_direction[1],
                        ),
                        current_direction,
                        current_cost + 1,
                    )
                )

            for neigbor in NEIGHBORS:
                if neigbor == current_direction:
                    continue
                if (neigbor[0] + current_direction[0]) == 0 and (
                    neigbor[1] + current_direction[1]
                ) == 0:  # 180° turn
                    continue
                if (
                    maze[current_pos[0] + neigbor[0]][current_pos[1] + neigbor[1]]
                    == "."
                ):
                    print("appending")
                    queue.append(
                        (
                            (current_pos[0] + neigbor[0], current_pos[1] + neigbor[1]),
                            neigbor,
                            current_cost + 1001,
                        )
                    )
        connections[this_node] = this_connections
    return connections


if __name__ == "__main__":
    data = read_maze("d16_sample.txt")
    pprint(data)
    print(find_next_nodes2(data))
