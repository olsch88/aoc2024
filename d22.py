def read_numbers(file:str)->list[int]:
    with open(file, "r")as f:
        data=[int(line)for line in f.readlines()]
        
    return data


def process_secret_number(secret: int)-> int:
    # mix
    secret=secret ^ (secret*64)
    # prune
    secret = secret%16777216
    
    # mix
    secret=secret ^ (secret//32)
    # prune
    secret = secret % 16777216

    # mix
    secret=secret ^ (secret*2048)
    # prune
    secret = secret%16777216
    
    return secret


def solve_part1(secrets: list[int])-> int:
    sum_of_secrets=0
    for secret in secrets:
        for _ in range(2000):
            secret=process_secret_number(secret)
        sum_of_secrets+=secret
    return sum_of_secrets
        


if __name__=="__main__":
    data=read_numbers("d22_input.txt")
    
    print(solve_part1(data))