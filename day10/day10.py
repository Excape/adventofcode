from functools import reduce

pairs = {"[": "]", "{": "}", "(": ")", "<": ">"}
scoring_1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
scoring_2 = {")": 1, "]": 2, "}": 3, ">": 4}


def part_1(input):
    illegal_chars = list(map(find_illegal_char, input))
    score = calc_points_1(illegal_chars)
    print(f"score: {score}")


def part_2(input):
    incomplete_lines = list(filter(lambda l: find_illegal_char(l) is None, input))
    extensions = list(map(complete_line, incomplete_lines))
    scores = list(map(calc_points_2, extensions))
    middle_score = sorted(scores)[int(len(scores) / 2)]
    print(f"middle score: {middle_score}")


def find_illegal_char(line):
    s = []
    for c in line:
        if c in pairs:
            s.append(c)
        else:
            if not s:
                return c
            match = s.pop()
            if pairs[match] != c:
                return c


def complete_line(line):
    s = []
    for c in line:
        if c in pairs:
            s.append(c)
        else:
            s.pop()
    return list(reversed([pairs[c] for c in s]))


def calc_points_1(illegal_chars):
    return sum(scoring_1[c] for c in illegal_chars if c in scoring_1)


def calc_points_2(extension):
    return reduce(lambda score, e: score * 5 + scoring_2[e], extension, 0)


with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]
    input = [[c for c in line] for line in lines]
    part_1(input)
    part_2(input)
