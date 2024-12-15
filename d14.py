from dataclasses import dataclass
import time
from math import lcm


@dataclass
class Robot:
    pos_x: int
    pos_y: int
    vel_x: int
    vel_y: int

    def move(self, limit_x, limit_y):
        self.pos_x = (self.pos_x + self.vel_x) % limit_x
        self.pos_y = (self.pos_y + self.vel_y) % limit_y


def read_input(filename: str) -> list[Robot]:
    with open(filename, "r") as f:
        raw_data = f.readlines()
    robots = []
    for line in raw_data:
        pos = line.split()[0]
        vel = line.split()[1]
        pos = pos.split("=")[1]
        pos_x = int(pos.split(",")[0])
        pos_y = int(pos.split(",")[1])
        vel = vel.strip().split("=")[1]
        vel_x = int(vel.split(",")[0])
        vel_y = int(vel.split(",")[1])
        robots.append(Robot(pos_x, pos_y, vel_x, vel_y))
    return robots


def get_safety_factor(robots: list[Robot], limit_x: int, limit_y: int) -> int:
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for robot in robots:
        if robot.pos_x < limit_x // 2 and robot.pos_y < limit_y // 2:
            q1 += 1
        elif robot.pos_x > limit_x / 2 and robot.pos_y < limit_y // 2:
            q2 += 1
        elif robot.pos_x > limit_x / 2 and robot.pos_y > limit_y / 2:
            q3 += 1
        elif robot.pos_x < limit_x // 2 and robot.pos_y > limit_y / 2:
            q4 += 1
    return q1 * q2 * q3 * q4


def calc_variance(robots: list[Robot]) -> tuple[int, int]:
    positions_x = []
    positions_y = []
    for robot in robots:
        positions_x.append(robot.pos_x)
        positions_y.append(robot.pos_y)
    mean_x = sum(positions_x) / len(positions_x)
    mean_y = sum(positions_y) / len(positions_y)
    var_x = sum([(x - mean_x) ** 2 for x in positions_x])
    var_y = sum([(y - mean_y) ** 2 for y in positions_y])
    return (var_x, var_y)


def solve_part1(robots: list[Robot]) -> int:
    limit_x = 101
    limit_y = 103
    for _ in range(100):
        for robot in robots:
            robot.move(limit_x, limit_y)
    return get_safety_factor(robots, limit_x, limit_y)


def solve_part2(robots: list[Robot]) -> int:
    limit_x = 101
    limit_y = 103

    factors = []
    for _ in range(10000):
        for robot in robots:
            robot.move(limit_x, limit_y)
        factors.append(get_safety_factor(robots, limit_x, limit_y))
    return factors.index(min(factors)) + 1


if __name__ == "__main__":
    start = time.perf_counter()
    data = read_input("d14_input.txt")
    print(solve_part1(data))
    print(f"Runtime: {time.perf_counter()-start}")
    start = time.perf_counter()
    data = read_input("d14_input.txt")
    print(solve_part2(data))
    print(f"Runtime: {time.perf_counter()-start}")
