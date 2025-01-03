def read_register(file: str) -> dict[str, int]:
    with open(file, "r") as f:
        raw_data = f.readlines()
    registers = dict()
    for line in raw_data:
        if line == "\n":
            break
        parts = line.split(":")
        registers[parts[0].split(" ")[1]] = int(parts[1])
    return registers


def read_program(file: str) -> list[int]:
    with open(file, "r") as f:
        raw_data = f.readlines()
    program = []
    for line in raw_data:
        if "Program" not in line:
            continue
        raw_program = line.split(":")[1]

    return list(int(i) for i in raw_program.split(","))


def solve_part1(registers: dict[str, int], program: list[int]) -> None:
    instruction_pointer = 0

    while instruction_pointer < len(program):
        instruction = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        combo = [0, 1, 2, 3, registers["A"], registers["B"], registers["C"]]
        match instruction:
            case 0:
                result = registers["A"] / (2 ** combo[operand])
                registers["A"] = int(result)
                instruction_pointer += 2
            case 1:
                registers["B"] = registers["B"] ^ operand
                instruction_pointer += 2
            case 2:
                registers["B"] = combo[operand] % 8
                instruction_pointer += 2
            case 3:
                if registers["A"] == 0:
                    instruction_pointer += 2
                else:
                    instruction_pointer = operand
            case 4:
                registers["B"] = registers["B"] ^ registers["C"]
                instruction_pointer += 2
            case 5:
                value = combo[operand] % 8
                print(value, end=",")
                instruction_pointer += 2
            case 6:
                result = registers["A"] / (combo[operand] ** 2)
                registers["B"] = int(result)
                instruction_pointer += 2
            case 7:
                result = registers["A"] / (combo[operand] ** 2)
                registers["C"] = int(result)
                instruction_pointer += 2

        

if __name__ == "__main__":
    registers = read_register("d17_input.txt")
    program = read_program("d17_input.txt")
    solve_part1(registers, program)
