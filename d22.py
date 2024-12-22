def read_numbers(file:str)->list[int]:
    with open(file, "r")as f:
        data=[int(line)for line in f.readlines()]
        
    return data

def process_secret_number(secret: int)-> int:
    


if __name__=="__main__":
    print(read_numbers("d22_sample.txt"))