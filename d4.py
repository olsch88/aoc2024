def read_data(filename: str) -> dict[tuple[int, int], str]:
    with open(filename, "r") as f:
        data = f.readlines()
    data_dict = dict()
    height = len(data)
    width = len(data[0].strip())
    for row_num, row in enumerate(data):
        for col_num, character in enumerate(row):
            data_dict[(row_num, col_num)] = character

    return data_dict, height, width


def solve_part1(data: dict, max_rows: int, max_col: int) -> int:
    counter = 0
    for row_index in range(max_rows):
        for col_index in range(max_col):
            if data[(row_index, col_index)] == "X":
                # down
                if (
                    data.get((row_index + 1, col_index), ".") == "M"
                    and data.get((row_index + 2, col_index), ".") == "A"
                    and data.get((row_index + 3, col_index), ".") == "S"
                ):
                    counter += 1
                # up
                if (
                    data.get((row_index - 1, col_index), ".") == "M"
                    and data.get((row_index - 2, col_index), ".") == "A"
                    and data.get((row_index - 3, col_index), ".") == "S"
                ):
                    counter += 1
                # right
                if (
                    data.get((row_index, col_index+1), ".") == "M"
                    and data.get((row_index, col_index+2), ".") == "A"
                    and data.get((row_index, col_index+3), ".") == "S"
                ):
                    counter += 1
                # left
                if (
                    data.get((row_index, col_index-1), ".") == "M"
                    and data.get((row_index, col_index-2), ".") == "A"
                    and data.get((row_index, col_index-3), ".") == "S"
                ):
                    counter += 1
                # down, right
                if (
                    data.get((row_index + 1, col_index+1), ".") == "M"
                    and data.get((row_index + 2, col_index+2), ".") == "A"
                    and data.get((row_index + 3, col_index+3), ".") == "S"
                ):
                    counter += 1
                # up right
                if (
                    data.get((row_index - 1, col_index+1), ".") == "M"
                    and data.get((row_index - 2, col_index+2), ".") == "A"
                    and data.get((row_index - 3, col_index+3), ".") == "S"
                ):
                    counter += 1
                # down, left
                if (
                    data.get((row_index+1, col_index-1), ".") == "M"
                    and data.get((row_index+2, col_index-2), ".") == "A"
                    and data.get((row_index+3, col_index-3), ".") == "S"
                ):
                    counter += 1
                # up left
                if (
                    data.get((row_index-1, col_index-1), ".") == "M"
                    and data.get((row_index-2, col_index-2), ".") == "A"
                    and data.get((row_index-3, col_index-3), ".") == "S"
                ):
                    counter += 1
    return counter


def solve_part2(data: dict, max_rows: int, max_col: int) -> int:
    counter = 0
    for row_index in range(max_rows):
        for col_index in range(max_col):
            if data[(row_index, col_index)] == "A":
                # down
                if (
                    data.get((row_index + 1, col_index+1), ".") == "M"
                    and data.get((row_index + 1, col_index-1), ".") == "S"
                    and data.get((row_index - 1, col_index+1), ".") == "M"
                    and data.get((row_index - 1, col_index-1), ".") == "S"
                    
                ):
                    counter += 1
                if (
                    data.get((row_index + 1, col_index+1), ".") == "M"
                    and data.get((row_index + 1, col_index-1), ".") == "M"
                    and data.get((row_index - 1, col_index+1), ".") == "S"
                    and data.get((row_index - 1, col_index-1), ".") == "S"
                    
                ):
                    counter += 1
                if (
                    data.get((row_index + 1, col_index+1), ".") == "S"
                    and data.get((row_index + 1, col_index-1), ".") == "S"
                    and data.get((row_index - 1, col_index+1), ".") == "M"
                    and data.get((row_index - 1, col_index-1), ".") == "M"
                    
                ):
                    counter += 1
                if (
                    data.get((row_index + 1, col_index+1), ".") == "S"
                    and data.get((row_index + 1, col_index-1), ".") == "M"
                    and data.get((row_index - 1, col_index+1), ".") == "S"
                    and data.get((row_index - 1, col_index-1), ".") == "M"
                    
                ):
                    counter += 1
    return counter

if __name__ == "__main__":
    data, max_row, max_col = read_data("d4_sample_2.txt")
    solve_part1(data, max_row, max_col)
    data, max_row, max_col = read_data("d4_input.txt")
    print(solve_part1(data, max_row, max_col))
    data, max_row, max_col = read_data("d4_input.txt")
    print(solve_part2(data, max_row, max_col))