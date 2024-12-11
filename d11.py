def read_data(filename:str)->list[int]:
    with open(filename, "r") as f:
        raw_data= f.readline()
    data = [int(num) for num in raw_data.strip().split()]
    
    return data


if __name__ =="__main__":
    print(read_data("d11_input.txt"))