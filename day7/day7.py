def find_min(input, part1):
    s = sorted(input)
    min = 100_000_000_000
    min_n = None
    for n in range(s[0], s[-1] + 1):
        cost = calc_cost_part1(n, s) if part1 else calc_cost_part2(n, s)
        if cost < min:
            min = cost
            min_n = n
    return min_n


def calc_cost_part1(n, input):
    return sum([abs(x - n) for x in input])


def calc_cost_part2(n, input):
    return sum([(abs(x - n) * (abs(x - n) + 1)) / 2 for x in input])


def solve_part1(input):
    result_pos = find_min(input, True)
    result_cost = calc_cost_part1(result_pos, input)
    print(f"the best position is {result_pos} with a cost of {result_cost}")


def solve_part2(input):
    result_pos = find_min(input, False)
    result_cost = calc_cost_part2(result_pos, input)
    print(f"the best position is {result_pos} with a cost of {result_cost}")


with open("input7.txt") as f:
    lines = f.readlines()
    input = list(map(int, lines[0].split(",")))
    solve_part1(input)
    solve_part2(input)
