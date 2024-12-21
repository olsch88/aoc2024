from collections import deque
import time
def read_towels(file: str) -> list[str]:
    with open(file, "r") as f:
        raw_data = f.readline()
    data = raw_data.strip().split(", ")
    return data


def read_designs(file: str) -> list[str]:
    with open(file, "r") as f:
        raw_data = f.readlines()
    designs = []
    for line in raw_data:
        if "," in line or line == "\n":
            continue
        designs.append(line.strip())
    return designs

def is_valid_bfs(design: str, towels: list[str])->bool:
    queue = deque()
    start = ""
    queue.append(start)
    target_len= len(design)
    
    while len(queue)>0:
        current_sample = queue.pop()
        current_len = len(current_sample)
        # print(len(queue))
        
        for towel in towels:
            if len(current_sample+towel)> target_len:
                continue
            if not design.startswith(current_sample+towel):
                continue
            # if design[current_len:current_len+len(towel)]!=towel:
            #     continue
            if current_sample+towel== design:
                return True
            queue.append(current_sample+towel)
        
        
    return False

def is_valid_bfs_part2(design: str, towels: list[str])->bool:
    queue = deque()
    start = ""
    queue.append(start)
    target_len= len(design)
    count_arrangements=0
    
    while len(queue)>0:
        current_sample = queue.pop()
        current_len = len(current_sample)
        # print(len(queue))
        
        for towel in towels:
            if len(current_sample+towel)> target_len:
                continue
            if not design.startswith(current_sample+towel):
                continue
            # if design[current_len:current_len+len(towel)]!=towel:
            #     continue
            if current_sample+towel== design:
                count_arrangements +=1
            queue.append(current_sample+towel)
        
    return count_arrangements


## unfinished try on dynamic programming
def is_valid(design: str, towels: list[str], tested: list = None) -> bool:
    # print(design)
    if not tested:
        tested = []
    if design in tested:
        return False
    tested.append(design)

    sep = len(design) // 2
    if design == "":
        return False

    for towel in towels:
        if design == towel:
            print(f"{design} is valid")
            return True

    return (
        (is_valid(design[:1], towels, tested) and is_valid(design[1:], towels, tested))
        or (
            is_valid(design[:2], towels, tested)
            and is_valid(design[2:], towels, tested)
        )
        or (
            is_valid(design[:3], towels, tested)
            and is_valid(design[3:], towels, tested)
        )
    )

def reduce_towels(design:str, towels:list[str])-> list[str]:
    reduced=[t for t in towels if t in design]
    return reduced
    

def solve_part1(towels, designs) -> int:
    valid_counter = 0
    for design in designs:
        reduced_towels = reduce_towels(design, towels)
        valid = is_valid_bfs(design, reduced_towels)
        
        # start= time.perf_counter()
        # valid = is_valid_bfs(design, towels)
        # print(f"time: {time.perf_counter()-start}")
        if valid:
            valid_counter += 1
    return valid_counter

def solve_part2(towels, designs) -> int:
    valid_counter = 0
    for design in designs:
        print(design)
        reduced_towels = reduce_towels(design, towels)
        valid_counter += is_valid_bfs_part2(design, reduced_towels)
        

    return valid_counter



if __name__ == "__main__":
    
    towels = read_towels("d19_input.txt")

    designs = read_designs("d19_input.txt")
    # print(designs)
    start = time.perf_counter()
    print(solve_part1(towels, designs))
    print(f"time: {time.perf_counter()-start}")
    
    towels = read_towels("d19_input.txt")

    designs = read_designs("d19_input.txt")
    print(solve_part2(towels, designs))