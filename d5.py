from collections import deque


def read_ordering(filename: str) -> dict:
    # ordering=defaultdict([])
    ordering: dict[int, list] = dict()
    with open(filename, "r") as f:
        data = f.readlines()
    for line in data:
        if line == "\n":
            break

        left_part = int(line.strip().split("|")[0])
        right_part = int(line.strip().split("|")[1])
        if left_part not in ordering.keys():
            ordering[left_part] = [right_part]
        else:
            ordering[left_part].append(right_part)
    return ordering


def read_pages(filename: str) -> list[list]:
    with open(filename, "r") as f:
        data = f.readlines()
    manuals = []
    for line in data:
        if "|" in line:
            continue
        if line == "\n":
            continue
        manuals.append([int(num) for num in line.strip().split(",")])
    return manuals


def find_path(graph: dict, start: int, end: int) -> bool:
    queue = deque()
    queue.append(start)
    while len(queue) > 0:
        current = queue.popleft()
        if current == end:
            return True
        if graph.get(current) == None:
            continue
        for target in graph.get(current):
            queue.append(target)
    return False

def find_path_v2(graph: dict, start: int, end: int) -> bool:
    if graph.get(start)==None:
        return False
    if end in graph[start]:
        return True
    return False

def is_manual_orderd(order:dict, manual: list[int])->bool:
    for i in range(1,len(manual)):
        if not find_path_v2(order, manual[i-1], manual[i]):
            return False
    return True
        

def order_manual(order:dict, manual:list[int])->list[int]:
    new_manual = manual.copy()
    for i in range(1,len(manual)):
        if not find_path_v2(order, new_manual[i-1], new_manual[i]):
            new_manual[i], new_manual[i-1]=new_manual[i-1], new_manual[i]
    return new_manual

def solve_part1(filename: str)->int:
    order = read_ordering(filename)
    manuals = read_pages(filename)
    middle_page_sum=0
    for manual in manuals:
        if is_manual_orderd(order, manual):
            middle_page_sum+=manual[(len(manual)-1)//2]
    return middle_page_sum

def solve_part2(filename: str)->int:
    order = read_ordering(filename)
    manuals = read_pages(filename)
    middle_page_sum=0
    for manual in manuals:
        if is_manual_orderd(order,manual):
            continue
        this_manual =manual.copy()
        while not is_manual_orderd(order,this_manual):
            orderd_manual=order_manual(order, this_manual)
            this_manual= orderd_manual
            
        middle_page_sum+=this_manual[(len(this_manual)-1)//2]
    return middle_page_sum

if __name__ == "__main__":
    ordering = read_ordering("d5_sample.txt")
    print(find_path(ordering, 97, 13))
    print(find_path(ordering, 13, 97))

    print(read_pages("d5_sample.txt"))
    print(solve_part1("d5_sample.txt"))
    print(solve_part1("d5_input.txt"))
    print("\n")
    
    print(solve_part2("d5_input.txt"))