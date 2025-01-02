import time
from collections import defaultdict


def read_connections(file: str) -> dict[str, list[str]]:
    with open(file, "r") as f:
        raw_data = f.readlines()
    connections = defaultdict(list)
    for line in raw_data:
        part1, part2 = line.strip().split("-")
        connections[part1].append(part2)
        connections[part2].append(part1)
    return connections


def get_triples(connections: dict[str, list[str]]) -> list:
    triples = []
    for node, neighbors in connections.items():
        for neigbor in neighbors:
            if len(set(neighbors) & set(connections[neigbor])) > 0:
                print(len(set(neighbors) & set(connections[neigbor])))
                for element in set(neighbors) & set(connections[neigbor]):
                    if set([node, neigbor, element]) not in triples:
                        triples.append(set([node, neigbor, element]))
    return triples


def starts_with_t(triples: list[set]) -> int:
    starts_with_t_counter = 0
    for triple in triples:
        found = False
        for element in triple:
            if element[0] == "t":
                found = True
        starts_with_t_counter += found
    return starts_with_t_counter


def solve_part1(connections: dict[str, list[str]]) -> int:
    triples = get_triples(connections)
    return starts_with_t(triples)


if __name__ == "__main__":
    start = time.perf_counter()
    data = read_connections("d23_sample.txt")
    print(solve_part1(data))
    print(f"Runtime: {time.perf_counter()-start:.4f}")
    # 11011 to high part1
