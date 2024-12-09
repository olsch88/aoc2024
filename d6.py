DIRECTION={"up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}


def read_data(filename:str)-> dict[tuple[int, int], str]:
    with open(filename, "r") as f:
        raw_data=f.readlines()
    obstacles =dict()
    start_pos=(0,0)
    dimension=(len(raw_data), len(raw_data[0].strip()))
    for row_count, line in enumerate(raw_data):
        for col_count, pos in enumerate(line.strip()):
            if pos=="#":
                obstacles[(row_count, col_count)]="#"
            if pos =="^":
                start_pos=(row_count, col_count)
    return obstacles, start_pos, dimension

def turn_clockwise(direction):
    if direction==DIRECTION["up"]:
        return DIRECTION["right"]
    if direction==DIRECTION["down"]:
        return DIRECTION["left"]
    if direction==DIRECTION["right"]:
        return DIRECTION["down"]
    if direction==DIRECTION["left"]:
        return DIRECTION["up"]

def out_of_bounds(position:tuple[int, int], dimensions:tuple[int, int]):
    if position[0]<0 or position[0]>=dimensions[0] or position[1]<0 or position[1]>=dimensions[1]:
        return True
    return False

def solve_part1(obstacles: dict, start:tuple[int, int], dimension:tuple[int, int])->int:
    current_direction = DIRECTION["up"]
    current_position= start
    visited=set()
    while True:

        visited.add(current_position)
        next_step=(current_position[0]+current_direction[0],current_position[1]+current_direction[1] )
        if out_of_bounds(next_step, dimension):
            break
        if obstacles.get(next_step)=="#":
            current_direction=turn_clockwise(current_direction)
            continue
        current_position=next_step
    return len(visited)

if __name__=="__main__":
    print(solve_part1(*read_data("d6_input.txt")))
    