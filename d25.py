def read_keys_and_locks(file: str) -> tuple[list[int], list[int]]:
    with open(file, "r") as f:
        raw_data = f.readlines()
    current_key = []
    current_lock = []
    elements = []
    keys = []
    locks = []
    startet = False
    key = False
    lock = False
    current_element = [0, 0, 0, 0, 0]
    for line in raw_data:
        if not startet:
            if line.strip() == "#####":
                startet = True
                lock = True
                continue
            if line.strip() == ".....":
                startet = True
                key = True
                continue
        else:
            if line == "\n":
                if key:
                    key = False
                    keys.append(current_element.copy())
                    current_element = [0, 0, 0, 0, 0]
                    startet = False
                    continue
                if lock:
                    lock = False
                    locks.append(current_element.copy())
                    current_element = [0, 0, 0, 0, 0]
                    startet = False
                    continue
            else:
                for i, char in enumerate(line.strip()):
                    if char == "#":
                        current_element[i] += 1
    if key:
        key = False
        keys.append(current_element.copy())
        current_element = [0, 0, 0, 0, 0]
        startet = False
    if lock:
        lock = False
        locks.append(current_element.copy())
        current_element = [0, 0, 0, 0, 0]
        startet = False
    return keys, locks


def test_pair(lock: list[int], key: list[int]) -> bool:
    for i in range(5):
        if lock[i] + key[i] > 6:
            return False
    return True


def solve_part1(keys: list[int], locks: list[int]) -> int:
    count = 0
    for key in keys:
        for lock in locks:
            if test_pair(lock, key):
                count += 1
    return count


if __name__ == "__main__":
    keys, locks = read_keys_and_locks("d25_input.txt")
    print(solve_part1(keys, locks))
