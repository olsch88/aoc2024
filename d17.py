def read_register(file: str)-> dict[str, int]:
    with open(file, "r")as f:
        raw_data= f.readlines()
    registers=dict()
    for line in raw_data:
        if line =="\n":
            break
        parts= line.split(":")
        registers[parts[0].split(" ")[1]]=int(parts[1])
    return registers

def read_program(file: str)-> list[int]:
    with open(file, "r")as f:
        raw_data= f.readlines()
    program=[]
    for line in raw_data:
        if "Program" not in line:
            continue
        raw_program=line.split(":")[1]

    return list(int(i) for i in raw_program.split(","))

if __name__=="__main__":
    print(read_register("d17_sample.txt"))
    print(read_program("d17_sample.txt"))