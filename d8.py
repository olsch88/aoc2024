from itertools import combinations

def read_data(file:str)-> dict:
    with open(file, "r") as f:
        raw_data = f.readlines()
    data = dict()
    for row_num, row in enumerate(raw_data):
        for col_num, ch in enumerate(row.strip()):
            if ch==".":
                continue
            if ch not in data:
                data[ch]=[(row_num, col_num)]
            else:
                data[ch].append((row_num, col_num))
    return data, len(raw_data), len(raw_data[0].strip())


def get_antinode_coordinates(coordinates: list[tuple[int,int]])-> set[tuple[int, int]]:
    antinodes=set()
    for pos1, pos2 in combinations(coordinates, 2):

        dif_vector =(pos1[0]-pos2[0], pos1[1]-pos2[1])

        antinodes.add((pos1[0]+dif_vector[0],pos1[1]+dif_vector[1]))
        antinodes.add((pos2[0]-dif_vector[0],pos2[1]-dif_vector[1]))
    return antinodes

def get_antinode_coordinates_part2(coordinates: list[tuple[int,int]])-> set[tuple[int, int]]:
    antinodes=set()
    for pos1, pos2 in combinations(coordinates, 2):
        dif_vector =(pos1[0]-pos2[0], pos1[1]-pos2[1])
        for i in range(80):
            antinodes.add((pos1[0]+dif_vector[0]*i,pos1[1]+dif_vector[1]*i))
            antinodes.add((pos2[0]-dif_vector[0]*i,pos2[1]-dif_vector[1]*i))
    return antinodes

def discart_outliers(coordinates:set[tuple[int,int]], limit_row:int, limit_col:int):
    reduced_coordinates=set()
    for coor in coordinates:
        if 0<=coor[0]<limit_row and 0<=coor[1]<limit_col:
            reduced_coordinates.add(coor)
    
    return reduced_coordinates

def solve_part1(antennas: dict, row_limit, col_limit)-> int:
    total_coordinates=set()
    for key, value in antennas.items():
        total_coordinates=total_coordinates.union(get_antinode_coordinates(value))
    reduced = discart_outliers(total_coordinates, row_limit, col_limit)
    return len(reduced)

def solve_part2(antennas: dict, row_limit, col_limit)-> int:
    total_coordinates=set()
    for key, value in antennas.items():
        total_coordinates=total_coordinates.union(get_antinode_coordinates_part2(value))
    reduced = discart_outliers(total_coordinates, row_limit, col_limit)
    return len(reduced)


if __name__ == "__main__":
    data, row_limit, col_limit = read_data("d8_input.txt")
    print(solve_part1(data, row_limit, col_limit))
    print(solve_part2(data, row_limit, col_limit))