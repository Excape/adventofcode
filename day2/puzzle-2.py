from functools import reduce
from typing import List, Tuple


def parse_input(line: str):
    return tuple(line.split())


moves = {
    "forward": lambda x, y, m: (x + m, y),
    "down": lambda x, y, m: (x, y + m),
    "up": lambda x, y, m: (x, y - m),
}


def part_1(input: List[Tuple[str, str]]):
    moves = {
        "forward": lambda x, y, m: (x + m, y),
        "down": lambda x, y, m: (x, y + m),
        "up": lambda x, y, m: (x, y - m),
    }
    return reduce(lambda pos, i: moves[i[0]](pos[0], pos[1], int(i[1])), input, (0, 0))


def part_2(input: List[Tuple[str, str]]):
    moves = {
        "forward": lambda x, y, a, m: (x + m, y + (a * m), a),
        "down": lambda x, y, a, m: (x, y, a + m),
        "up": lambda x, y, a, m: (x, y, a - m),
    }

    return reduce(
        lambda pos, i: moves[i[0]](pos[0], pos[1], pos[2], int(i[1])), input, (0, 0, 0)
    )


with open("input2.txt") as f:
    lines = f.readlines()
    input = list(map(parse_input, lines))
    position = part_1(input)
    print(position)
    print(position[0] * position[1])

    position_2 = part_2(input)
    print(position_2)
    print(f"result: {position_2[0]*position_2[1]}")
