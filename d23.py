import time
from collections import defaultdict


def read_connections(file: str) -> dict[str, set[str]]:
    with open(file, "r") as f:
        raw_data = f.readlines()
    connections = defaultdict(set)
    for line in raw_data:
        part1, part2 = line.strip().split("-")
        connections[part1].add(part2)
        connections[part2].add(part1)
    return connections


def get_triples(connections: dict[str, set[str]]) -> list[set[str]]:
    triples = []
    for node, neighbors in connections.items():
        for neigbor in neighbors:
            if len(set(neighbors) & set(connections[neigbor])) > 0:
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
                break
        starts_with_t_counter += found
    return starts_with_t_counter


def find_maximal_clique(connections: dict[str, set[str]]):
    lan_members = set(connections.keys())
    i = 0
    max_set = set()

    def BronKerbosch(R: set, P: set, X: set, max_len=0, max_set=set()):
        if len(P) == 0 and len(X) == 0:
            if len(R) > 12:
                print(R)
                max_len = len(R)
                max_set = R
                print(",".join(sorted(R)))
            return R
        for member in P:
            BronKerbosch(
                R.union(set([member])),
                P.intersection(connections[member]),
                X.intersection(connections[member]),
                max_len,
                max_set,
            ),
            P = P.difference(set([member]))
            X = X.union(set([member]))

    BronKerbosch(R=set(), P=lan_members, X=set(), max_set=max_set)
    return max_set


def solve_part1(connections: dict[str, set[str]]) -> int:
    triples = get_triples(connections)
    return starts_with_t(triples)


def solve_part2(connections: dict[str, set[str]]) -> int:
    print(find_maximal_clique(connections))
    return 1


if __name__ == "__main__":
    start = time.perf_counter()
    data = read_connections("d23_input.txt")
    print(solve_part1(data))
    print(f"Runtime: {time.perf_counter()-start:.4f}")
    print(solve_part2(data))
