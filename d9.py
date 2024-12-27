import time

def read_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        raw_data = f.readline()
    data = [int(char) for char in raw_data]
    return data


def expand_disk(disk_map: list[int]):
    id_num = 0
    expanded_memory = []
    for i, number in enumerate(disk_map):
        if i % 2 == 0:
            expanded_memory.extend([id_num] * number)
            id_num += 1
        else:
            expanded_memory.extend([-1] * number)
    return expanded_memory


def get_last_number(disk_list: list[int]) -> int:
    return (
        len(disk_list)
        - min([disk_list[::-1].index(i) for i in range(max(disk_list) + 1)])
        - 1
    )


def swap_memory(extended_disk_map: list[int]) -> list[int]:
    number_empty = extended_disk_map.count(-1)
    new_disk_map = extended_disk_map.copy()
    # print(extended_disk_map)
    for i, number in enumerate(extended_disk_map):
        if number == -1:
            pos_insert=i

            pos_last_number = get_last_number(new_disk_map)
            if i >pos_last_number:
                break
            last_number = new_disk_map.pop(pos_last_number)
            
            new_disk_map.insert(pos_insert, last_number)
            # new_disk_map.pop(pos_insert + 1)
            new_disk_map.remove(-1)
            # print(new_disk_map)
    # print(new_disk_map)
    return new_disk_map

def get_last_empty(disk_map:list[int])-> int:
    return (        len(disk_map)-
        disk_map[::-1].index(-1)
        -1)

def swap_memory_v2(extended_disk_map: list[int]) -> list[int]:
    extended_disk_map = extended_disk_map[::-1]
    new_disk_map = extended_disk_map.copy()
    # print(new_disk_map)
    for i, number in enumerate(extended_disk_map):
        if number==-1:
            continue
        if -1 not in new_disk_map:
            break
        index_empty= get_last_empty(new_disk_map)
        
        new_disk_map.pop(index_empty)
        new_disk_map.insert(index_empty, number)
        new_disk_map.remove(number)
        # print(new_disk_map[::-1])
    return new_disk_map[::-1]

def swap_memory_part2(extended_disk_map:list[int]):
    original_disk_map = extended_disk_map.copy()
    new_disk_map = extended_disk_map.copy()
    extended_disk_map = extended_disk_map[::-1]

    current_number=0
    start_pos=999999
    stop_pos =-9999
    start_pos_insert=999999
    stop_pos_insert=-9999
    # getting the number to start with
    # print( extended_disk_map[0])
    for number in extended_disk_map:
        if number ==-1:
            continue
        current_number = number
        break
    while current_number!=0:
        # print (f"{current_number=}")
        start_pos=0
        stop_pos=0
        started=False
        for pos, number in enumerate(extended_disk_map):
            if number == current_number and not started:
                start_pos=pos
                started=True
            if number == current_number and pos > stop_pos:
                stop_pos= pos
            # if number !=current_number:
            #     started= False
        # print(start_pos, stop_pos)
        current_len = stop_pos-start_pos+1
        # print(f"{current_len=}")
        # find consecutive free space:

        started_insert=False
        start_pos_insert=0
        stop_pos_insert=-1
        for pos, number in enumerate(new_disk_map):
            if number == -1 and not started_insert:#and pos<=start_pos_insert:
                started_insert=True
                start_pos_insert=pos
                # print(start_pos_insert)
            if number == -1 and pos > stop_pos_insert:
                stop_pos_insert= pos
            if number !=-1:
                started_insert=False
            current_len_insert = stop_pos_insert-start_pos_insert+1
            if current_len_insert>=current_len:
                    break
            # if number != -1:
            #     start_pos_insert=pos
                
        if current_len_insert>= current_len and start_pos_insert< len(extended_disk_map)-stop_pos:
            for i in range(start_pos_insert, stop_pos_insert+1):
                new_disk_map   [i]=current_number
            for i in range(current_len):
                new_disk_map [len(original_disk_map)-1-stop_pos+i]=-1
        # print(start_pos_insert, stop_pos_insert, current_len_insert)
        #start_pos_insert=stop_pos_insert
        # print(new_disk_map)
        current_number-=1
    return new_disk_map

def calc_checksum(diskmap: list[int]) -> int:
    checksum = 0
    for i, number in enumerate(diskmap):
        if number !=-1:
            checksum += i *  number
    return checksum

def solve_part1(filename: str)-> int:
    data = read_data(filename)

    expanded = expand_disk(data)
    # print(expanded)
    new_map = swap_memory_v2(expanded)
    print(calc_checksum(new_map))

def solve_part2(filename: str)-> int:
    data = read_data(filename)

    expanded = expand_disk(data)
    
    new_map = swap_memory_part2(expanded)
    print(calc_checksum(new_map))

if __name__ == "__main__":
    # solve_part1("d9_sample.txt")
    start=time.perf_counter()
    solve_part1("d9_input.txt")
    print(f"runtime: {time.perf_counter()-start:.4f}")
    start=time.perf_counter()
    solve_part2("d9_input.txt")
    print(f"runtime: {time.perf_counter()-start:.4f}")