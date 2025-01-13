from dataclasses import dataclass

def read_values(file:str)->dict[str, int]:
    with open(file) as f:
        lines = f.readlines()
    wires= dict()
    for  line in lines:
        if line=="\n":
            break
        wire, value = line.strip().split(":")
        wires[wire] = int(value)
        

    return wires
@dataclass
class Connection():
    wire1:str
    wire2:str
    operator:str
    target:str

def read_connections(file:str)->list[Connection]:
    with open(file) as f:
        lines = f.readlines()
    connections = []
    for line in lines:
        if ":"in line:
            continue
        if line=="\n":
            continue
        wire1, operator, wire2,_, target = line.strip().split()
        
        connections.append(Connection(wire1, wire2, operator, target))
    return connections

def process_connections(connection: list[Connection], values:dict[str, int]):
    unprocessed = connection.copy()
    
    while unprocessed:
        to_be_removed = []
        for conn in unprocessed:
            if conn.wire1 in values and conn.wire2 in values:
                if conn.operator == "AND":
                    values[conn.target] = values[conn.wire1] & values[conn.wire2]
                elif conn.operator == "OR":
                    values[conn.target] = values[conn.wire1] | values[conn.wire2]
                elif conn.operator == "XOR":
                    values[conn.target] = values[conn.wire1] ^ values[conn.wire2]
                to_be_removed.append(conn)
        for con in to_be_removed:
            unprocessed.remove(con)
    return values

def solve_part1(connections, values)-> int:
    values = process_connections(connections, values)
    z_values = {key: value for key, value in values.items() if "z" in key}
    print(z_values)
    binary=""
    print(dict(sorted(z_values.items(),reverse=True)))
    for _, value in dict(sorted(z_values.items(),reverse=True)).items():
        print(value)
        binary+=str(value)
    return int(binary,base=2)


if __name__ == "__main__":
    values =read_values("d24_input.txt")
    print(read_values("d24_sample2.txt")) # {'a': 1, 'b': 2, '
    connections=read_connections("d24_input.txt")    
    print(solve_part1(connections, values))